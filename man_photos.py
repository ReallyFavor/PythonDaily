import requests
import re
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import rarfile
import shutil

def get_page_content(url):
    """使用requests模拟curl请求获取页面内容"""
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://sc.chinaz.com/tupian/shuaigetupian_3.html',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
    }
    
    cookies = {
        'ASP.NET_SessionId': 'l3ehdhhcgbtqgmbqvnmyreci'
    }
    
    response = requests.get(url, headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    return response.text

def convert_url_to_big_image(origin_url):
    """将origin_url转换为高清图片链接"""
    # origin_url 来源于html中的 div.item>img 的data-original属性
    # 提取路径部分，然后使用新域名topic.chinaz.net
    
    # 去掉协议部分
    if origin_url.startswith('http://'):
        origin_url = origin_url[7:]
    elif origin_url.startswith('https://'):
        origin_url = origin_url[8:]
    elif origin_url.startswith('//'):
        origin_url = origin_url[2:]
    
    # 找到第一个斜杠的位置，提取路径部分
    if '/' in origin_url:
        path_part = origin_url[origin_url.find('/'):]
    else:
        # 如果没有路径，直接返回
        return None
    
    # 替换_s.jpg为_big.jpg，_s.png为_big.png
    path_part = path_part.replace('_s.jpg', '_big.jpg').replace('_s.png', '_big.png')
    
    # 使用新域名构建完整URL
    url = 'https://tppic.chinaz.net' + path_part
    
    return url

def extract_image_urls(html_content):
    """从HTML内容中提取图片URL"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 查找所有div.item下的img标签
    items = soup.select('div.item img')
    
    image_urls = []
    for img in items:
        data_original = img.get('data-original')
        if data_original:
            # 转换为高清图片链接
            big_image_url = convert_url_to_big_image(data_original)
            image_urls.append({
                'original': data_original,
                'big_image': big_image_url,
                'alt': img.get('alt', '')
            })
    
    return image_urls

def download_image(url, filename, download_dir='man_photos'):
    """下载图片"""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # 检查最终的图片文件是否已存在
    final_image_path = os.path.join(download_dir, filename)
    if os.path.exists(final_image_path):
        print(f"文件已存在: {filename}")
        return True
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
        }
        
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        filepath = os.path.join(download_dir, filename)
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"成功下载: {filename}")
        return True
        
    except Exception as e:
        print(f"直接下载图片失败: {str(e)}，尝试下载rar文件...")
        
        # 尝试下载rar文件
        rar_url = url.replace('tppic.chinaz.net/Files/pic', 'downsc.chinaz.net/Files/Download').replace('_big.jpg', '.rar').replace('_big.png', '.rar')
        rar_filename = filename.replace('.jpg', '.rar').replace('.png', '.rar')
        rar_filepath = os.path.join(download_dir, rar_filename)
        
        try:
            print(f"正在下载rar文件: {rar_filename}")
            rar_response = requests.get(rar_url, headers=headers, stream=True)
            rar_response.raise_for_status()
            
            # 检查内容长度
            content_length = rar_response.headers.get('content-length')
            if content_length:
                print(f"rar文件大小: {int(content_length)} 字节")
            
            with open(rar_filepath, 'wb') as f:
                downloaded_size = 0
                for chunk in rar_response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
            
            print(f"rar文件下载成功: {rar_filename} (实际下载: {downloaded_size} 字节)")
            
            # 验证文件大小
            actual_size = os.path.getsize(rar_filepath)
            if content_length and actual_size != int(content_length):
                print(f"警告: 文件大小不匹配，预期: {content_length}, 实际: {actual_size}")
            
            # 如果文件太小，可能是错误页面
            if actual_size < 1000:  # 小于1KB可能是错误信息
                print(f"rar文件太小 ({actual_size} 字节)，可能下载失败")
                os.remove(rar_filepath)
                return False
            
            # 解压缩rar文件
            try:
                print(f"正在解压缩: {rar_filename}")
                
                # 先检查rar文件是否有效
                try:
                    with rarfile.RarFile(rar_filepath) as rf:
                        if rf.needs_password():
                            print(f"rar文件需要密码，跳过")
                            os.remove(rar_filepath)
                            return False
                        
                        # 测试rar文件完整性
                        try:
                            rf.testrar()
                            print("rar文件完整性检查通过")
                        except Exception as test_e:
                            print(f"rar文件完整性检查失败: {str(test_e)}")
                            # 尝试继续解压，有时测试失败但实际可以解压
                        
                        # 获取rar文件中的所有文件
                        file_list = rf.namelist()
                        print(f"rar文件中包含的文件: {file_list}")
                        
                        # 查找图片文件
                        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
                        image_files = [f for f in file_list if any(f.lower().endswith(ext) for ext in image_extensions)]
                        
                        if image_files:
                            # 提取第一个图片文件
                            image_file = image_files[0]
                            print(f"找到图片文件: {image_file}")
                            
                            # 创建临时目录
                            temp_dir = os.path.join(download_dir, 'temp_extract')
                            if not os.path.exists(temp_dir):
                                os.makedirs(temp_dir)
                            
                            try:
                                # 提取到临时目录
                                rf.extract(image_file, temp_dir)
                                
                                # 获取提取的文件路径
                                extracted_path = os.path.join(temp_dir, image_file)
                                if os.path.exists(extracted_path):
                                    # 移动到最终位置
                                    shutil.move(extracted_path, final_image_path)
                                    print(f"成功提取并重命名图片: {filename}")
                                    
                                    # 清理临时目录
                                    shutil.rmtree(temp_dir, ignore_errors=True)
                                    
                                    # 删除rar文件
                                    os.remove(rar_filepath)
                                    print(f"已删除临时rar文件: {rar_filename}")
                                    
                                    return True
                                else:
                                    print(f"提取失败: 找不到提取的文件 {extracted_path}")
                            
                            except Exception as extract_e:
                                print(f"文件提取失败: {str(extract_e)}")
                                # 清理临时目录
                                shutil.rmtree(temp_dir, ignore_errors=True)
                        else:
                            print(f"rar文件中没有找到图片文件")
                            
                except rarfile.RarCannotExec:
                    print("错误: 系统中没有安装rar解压工具")
                    print("请安装unrar: brew install unrar (macOS) 或 apt-get install unrar (Ubuntu)")
                    return False
                except rarfile.BadRarFile:
                    print(f"错误: {rar_filename} 不是有效的rar文件")
                    os.remove(rar_filepath)
                    return False
                except Exception as rar_open_e:
                    print(f"打开rar文件失败: {str(rar_open_e)}")
                    os.remove(rar_filepath)
                    return False
                        
            except Exception as rar_e:
                print(f"解压缩rar文件失败: {str(rar_e)}")
                # 如果解压失败，删除损坏的rar文件
                if os.path.exists(rar_filepath):
                    os.remove(rar_filepath)
                
        except Exception as rar_download_e:
            print(f"下载rar文件失败: {str(rar_download_e)}")
        
        return False

def main(start_page=1, end_page=10):
    """主函数
    
    Args:
        start_page (int): 开始页面编号，默认为1
        end_page (int): 结束页面编号，默认为10
    """
    # 设置要下载的页面范围
    
    print(f"开始批量下载第 {start_page} 到第 {end_page} 页的图片...")
    
    total_downloaded = 0
    
    for page in range(start_page, end_page + 1):
        # 构造每页的URL
        if page == 1:
            target_url = f"https://sc.chinaz.com/tupian/shuaigetupian.html"
        else:
            target_url = f"https://sc.chinaz.com/tupian/shuaigetupian_{page}.html"
        
        print(f"\n{'='*50}")
        print(f"正在处理第 {page} 页...")
        print(f"URL: {target_url}")
        print(f"{'='*50}")
        
        try:
            print("正在获取网页内容...")
            html_content = get_page_content(target_url)
            
            print("正在解析图片链接...")
            image_urls = extract_image_urls(html_content)
            
            print(f"第 {page} 页找到 {len(image_urls)} 张图片")
            
            if len(image_urls) == 0:
                print(f"第 {page} 页没有找到图片，跳过...")
                continue
            
            # 为每页创建单独的文件夹
            page_dir = f"man_photos"
            
            # 下载图片
            for i, img_info in enumerate(image_urls, 1):
                print(f"正在下载第 {page} 页的第 {i}/{len(image_urls)} 张图片...")
                
                # 从URL中提取文件名，并添加页码前缀
                filename = os.path.basename(img_info['big_image'])
                if not filename.endswith('.jpg') and not filename.endswith('.png'):
                    filename += '.jpg'
                
                # 添加页码前缀避免文件名冲突
                filename = f"page{page}_{filename}"
                
                # 下载图片
                if download_image(img_info['big_image'], filename, page_dir):
                    total_downloaded += 1
                
                # 避免请求过快，添加延迟
                time.sleep(1)
            
            print(f"第 {page} 页下载完成！")
            
        except Exception as e:
            print(f"处理第 {page} 页时出错: {str(e)}")
            continue
        
        # 页面间添加稍长的延迟
        time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"所有页面处理完成！总共下载了 {total_downloaded} 张图片")
    print(f"{'='*60}")

if __name__ == "__main__":
    # 默认下载第1页到第10页
    main(17,55)
    
    # 如果要自定义页面范围，可以这样调用：
    # main(start_page=1, end_page=5)  # 只下载第1-5页
    # main(start_page=3, end_page=8)  # 只下载第3-8页