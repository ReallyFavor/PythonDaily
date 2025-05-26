#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片下载器
支持从URL列表或JSON文件下载图片
"""

import requests
import json
import time
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageDownloader:
    def __init__(self, max_workers=5, timeout=30):
        """
        初始化图片下载器
        
        Args:
            max_workers (int): 最大并发下载数
            timeout (int): 下载超时时间
        """
        self.max_workers = max_workers
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'Referer': 'https://stock.tuchong.com/'
        }
    
    def download_single_image(self, image_url, save_path, retries=3):
        """
        下载单张图片
        
        Args:
            image_url (str): 图片URL
            save_path (str): 保存路径
            retries (int): 重试次数
        
        Returns:
            tuple: (成功状态, 图片URL, 保存路径, 错误信息)
        """
        for attempt in range(retries + 1):
            try:
                # 创建保存目录
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                # 检查文件是否已存在
                if os.path.exists(save_path):
                    file_size = os.path.getsize(save_path)
                    if file_size > 0:  # 文件存在且不为空
                        return True, image_url, save_path, "文件已存在"
                
                # 下载图片
                response = requests.get(image_url, headers=self.headers, timeout=self.timeout, stream=True)
                response.raise_for_status()
                
                # 检查内容类型
                content_type = response.headers.get('content-type', '')
                if not content_type.startswith('image/'):
                    return False, image_url, save_path, f"非图片内容: {content_type}"
                
                # 保存图片
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                file_size = os.path.getsize(save_path)
                if file_size == 0:
                    os.remove(save_path)
                    return False, image_url, save_path, "下载的文件为空"
                
                return True, image_url, save_path, f"下载成功 ({file_size} bytes)"
                
            except requests.exceptions.RequestException as e:
                if attempt < retries:
                    logger.warning(f"下载失败，重试 {attempt + 1}/{retries}: {image_url}")
                    time.sleep(1)
                    continue
                return False, image_url, save_path, f"下载失败: {e}"
            except Exception as e:
                return False, image_url, save_path, f"保存失败: {e}"
        
        return False, image_url, save_path, "超过最大重试次数"
    
    def download_from_urls(self, urls, save_dir, filename_func=None, use_threading=True):
        """
        从URL列表下载图片
        
        Args:
            urls (list): 图片URL列表
            save_dir (str): 保存目录
            filename_func (function): 生成文件名的函数，接收URL参数
            use_threading (bool): 是否使用多线程
        
        Returns:
            dict: 下载统计信息
        """
        if filename_func is None:
            filename_func = lambda url: os.path.basename(url).split('?')[0]
        
        stats = {
            'total': len(urls),
            'success': 0,
            'failed': 0,
            'skipped': 0
        }
        
        tasks = []
        for url in urls:
            filename = filename_func(url)
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                filename += '.jpg'  # 默认扩展名
            
            save_path = os.path.join(save_dir, filename)
            tasks.append((url, save_path))
        
        logger.info(f"开始下载 {stats['total']} 张图片到 {save_dir}")
        
        if use_threading and len(tasks) > 1:
            # 多线程下载
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_task = {
                    executor.submit(self.download_single_image, url, save_path): (url, save_path)
                    for url, save_path in tasks
                }
                
                for future in as_completed(future_to_task):
                    url, save_path = future_to_task[future]
                    try:
                        success, _, _, message = future.result()
                        if success:
                            if "已存在" in message:
                                stats['skipped'] += 1
                            else:
                                stats['success'] += 1
                            logger.info(f"✓ {os.path.basename(save_path)}: {message}")
                        else:
                            stats['failed'] += 1
                            logger.error(f"✗ {os.path.basename(save_path)}: {message}")
                    except Exception as e:
                        stats['failed'] += 1
                        logger.error(f"✗ {os.path.basename(save_path)}: 处理失败 {e}")
        else:
            # 单线程下载
            for i, (url, save_path) in enumerate(tasks, 1):
                logger.info(f"正在下载 {i}/{stats['total']}: {os.path.basename(save_path)}")
                
                success, _, _, message = self.download_single_image(url, save_path)
                if success:
                    if "已存在" in message:
                        stats['skipped'] += 1
                    else:
                        stats['success'] += 1
                    logger.info(f"✓ {message}")
                else:
                    stats['failed'] += 1
                    logger.error(f"✗ {message}")
                
                # 添加延迟避免请求过快
                if i < stats['total']:
                    time.sleep(0.5)
        
        logger.info(f"下载完成！成功: {stats['success']}, 跳过: {stats['skipped']}, 失败: {stats['failed']}")
        return stats
    
    def download_from_json(self, json_file, save_dir, image_id_key='image_id'):
        """
        从JSON文件下载图片
        
        Args:
            json_file (str): JSON文件路径
            save_dir (str): 保存目录
            image_id_key (str): 图片ID的字段名
        
        Returns:
            dict: 下载统计信息
        """
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            urls = []
            for item in data:
                image_id = item.get(image_id_key, '')
                if image_id:
                    # 构造图虫网的图片URL
                    image_url = f"https://cdn9-banquan.ituchong.com/weili/image/l/{image_id}.jpeg"
                    urls.append(image_url)
            
            if not urls:
                logger.error(f"从 {json_file} 中未找到有效的图片URL")
                return {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}
            
            logger.info(f"从 {json_file} 中解析出 {len(urls)} 个图片URL")
            
            # 定义文件名生成函数
            def filename_func(url):
                # 从URL中提取image_id作为文件名
                if '/image/l/' in url:
                    image_id = url.split('/image/l/')[-1].split('.')[0]
                    return f"{image_id}.jpeg"
                return os.path.basename(url)
            
            return self.download_from_urls(urls, save_dir, filename_func, use_threading=True)
            
        except Exception as e:
            logger.error(f"处理JSON文件失败: {e}")
            return {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}
    
    def download_from_txt(self, txt_file, save_dir):
        """
        从文本文件下载图片（每行一个URL）
        
        Args:
            txt_file (str): 文本文件路径
            save_dir (str): 保存目录
        
        Returns:
            dict: 下载统计信息
        """
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            if not urls:
                logger.error(f"从 {txt_file} 中未找到有效的URL")
                return {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}
            
            logger.info(f"从 {txt_file} 中读取到 {len(urls)} 个URL")
            
            return self.download_from_urls(urls, save_dir, use_threading=True)
            
        except Exception as e:
            logger.error(f"处理文本文件失败: {e}")
            return {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}

def main():
    """命令行主函数"""
    parser = argparse.ArgumentParser(description='图片下载器')
    parser.add_argument('--input', '-i', required=True, help='输入文件路径（JSON或TXT）')
    parser.add_argument('--output', '-o', default='downloaded_images', help='输出目录')
    parser.add_argument('--workers', '-w', type=int, default=5, help='并发下载数')
    parser.add_argument('--timeout', '-t', type=int, default=30, help='下载超时时间')
    
    args = parser.parse_args()
    
    # 创建下载器
    downloader = ImageDownloader(max_workers=args.workers, timeout=args.timeout)
    
    # 根据文件类型选择下载方法
    input_file = args.input
    if input_file.endswith('.json'):
        stats = downloader.download_from_json(input_file, args.output)
    elif input_file.endswith('.txt'):
        stats = downloader.download_from_txt(input_file, args.output)
    else:
        logger.error("不支持的文件类型，请使用 .json 或 .txt 文件")
        return
    
    # 显示统计信息
    total = stats['total']
    success = stats['success']
    failed = stats['failed']
    skipped = stats['skipped']
    
    print(f"\n=== 下载完成 ===")
    print(f"总计: {total}")
    print(f"成功: {success}")
    print(f"跳过: {skipped}")
    print(f"失败: {failed}")
    print(f"成功率: {success/total*100:.1f}%" if total > 0 else "成功率: 0%")

if __name__ == "__main__":
    # 如果直接运行，使用示例模式
    if len(os.sys.argv) == 1:
        logger.info("=== 图片下载器示例模式 ===")
        
        # 示例：下载图虫网图片
        downloader = ImageDownloader(max_workers=3, timeout=30)
        
        # 检查是否有现成的JSON文件
        json_files = [f for f in os.listdir('.') if f.endswith('_images.json')]
        if json_files:
            json_file = json_files[0]
            logger.info(f"找到JSON文件: {json_file}")
            
            save_dir = f"downloaded_images/{json_file.replace('_images.json', '_photos')}"
            stats = downloader.download_from_json(json_file, save_dir)
            
            print(f"\n=== 下载统计 ===")
            print(f"总计: {stats['total']}")
            print(f"成功: {stats['success']}")
            print(f"跳过: {stats['skipped']}")
            print(f"失败: {stats['failed']}")
        else:
            logger.info("未找到JSON文件，请先运行 tuchong_search.py 获取图片数据")
            logger.info("或使用命令行模式: python image_downloader.py -i 文件路径 -o 输出目录")
    else:
        main() 