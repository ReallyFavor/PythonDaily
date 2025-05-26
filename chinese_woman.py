import requests
import json
import time
import os

# 创建保存图片的目录
if not os.path.exists('chinese_woman_photos'):
    os.makedirs('chinese_woman_photos')

# 设置请求头
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.pexels.com/search/chinese%20woman/',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'secret-key': 'H2jk9uKnhRmL6WPwh89zBezWvr',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'x-client-type': 'react',
    'x-forwarded-cf-connecting-ip': '',
    'x-forwarded-cf-ipregioncode': '',
    'x-forwarded-http_cf_ipcountry': ''
}

# 设置cookies - 使用新的cookies
cookies = {
    'OptanonAlertBoxClosed': '2025-02-10T08:50:08.435Z',
    '_cfuvid': 'fgFgwSaTpYFfIFtwDaByE6QJGCfpeWfqDQ6q3Q2FG5E-1747879495416-0.0.1.1-604800000',
    'country-code-v2': 'SG',
    '__cf_bm': 'Zzblb7LxZmoNEwjQlK07obc4q164tLir8vT0uX3Mp2w-1747964057-1.0.1.1-7jiTNLxghxH9dZaIjq8fizVK8R6m.961sC1aGrmpCJGYjpBgZsgs0ldxLirqwx0wfc_Z2QpQrM2WSk670MhDreadKvZX3dv_.kyTz9V50qM',
    '_sp_ses.9ec1': '*',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+May+23+2025+09%3A34%3A20+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=SG%3B&AwaitingReconsent=false',
    'cf_clearance': 'hVDpsIL4De_lQ4jm2nrGFOpDV.jkh7MIeWxORmKwuXY-1747964060-1.2.1.1-40lRNmJQh9Qv3_N0qidbSm6iRErt1D.uiuZ6bICaVitGyNhySiQU9wUlphqIbcfe6mSYQNs1NC8X3mRVMcSu5elmFDu8enYMuT5vTYcKSnmCsHC0s_AWcA8xNtWRJIi9losedzVacADERM8.b5z.UwzzAqPenMzRnOe4n0n0cNnqLt0DAPLPWugAzm37hpJw6Wx9_x6NyXjafxdVrTUILBAnMGE8nYsYVPzHwXWwIyqcq7BM1ycmyAfRAInsJ.uFyTFEGdCoV4ATg0jQT0TEK2R5pl4CY2AOb.Qdrx.F7POyWVhREwL8HIbkbcAwWXRmIcJH1m.qPngNmEwfU5HoyxvLSurwe7o3GrYbAAbHDoQ',
    'g_state': '{"i_p":1747971263992,"i_l":1}',
    '_pexels_session': 'miOybJJs59pAgcskUSCb1sJOBkIX1Z5c64VX%2Bvan%2FP4Q30OJY5G0do2okKiJPYScIJdjx68BikwrOrc7N0e5SJwyHa9L6TPkCcr02jet6fe9z%2FeiCxPLuO0kPu%2Bquti%2B25JRRcnJ6rCe3FM5mZimcoV6fn1ikDXB5YisX9GabYXVuDMnge5Mgox%2FNcILlGQWiRctv%2FWeThyhUvYjKFREHAZ2JrdVJbMJpj0S--Q5g7vAFyfORVZQgU--hImkwtn4GtlhIyLL5MvmYQ%3D%3D',
    '_sp_id.9ec1': 'e74076d9-f202-4980-b6ec-310e5bd1a192.1739176397.4.1747964087.1747908644.97a8dba2-9abb-4cee-af80-5f3d2c162e60.c748aacd-c6ea-44bb-b9ab-a74bb9443d8e.232c1edc-0ff1-431b-9646-04b77d792238.1747964060226.4'
}

def download_image(url, filename):
    """下载图片并保存到本地"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"下载成功: {filename}")
            return True
        else:
            print(f"下载失败: {url}, 状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"下载出错: {url}, 错误: {str(e)}")
        return False

def get_photos(page, per_page=24):
    """获取指定页码的照片数据"""
    url = f"https://www.pexels.com/en-us/api/v3/search/photos"
    
    params = {
        "query": "chinese woman",  # 修改为中国女性
        "page": page,
        "per_page": per_page,
        "orientation": "all",
        "size": "all",
        "color": "all",
        "sort": "popular",
        "seo_tags": "true"
    }
    
    try:
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"请求失败: 页码 {page}, 状态码: {response.status_code}")
            return None
    except Exception as e:
        print(f"请求出错: 页码 {page}, 错误: {str(e)}")
        return None

def process_photos(data, download=True):
    """处理照片数据并可选择下载照片"""
    if not data or 'data' not in data:
        print("无有效数据")
        return []
    
    photos = []
    for item in data['data']:
        try:
            photo_info = {
                'id': item['id'],
                'width': item['attributes']['width'],
                'height': item['attributes']['height'],
                'url': item['attributes']['image']['download_link'],
                'download_url': item['attributes']['image']['download_link']
            }
            photos.append(photo_info)
            
            # 下载图片
            if download:
                filename = f"chinese_woman_photos/{photo_info['id']}.jpg"
                download_image(photo_info['download_url'], filename)
                # 暂停一下，避免请求过快
                time.sleep(0.5)
        except Exception as e:
            print(f"处理照片时出错: {str(e)}")
    
    return photos

def main():
    """主函数，获取多页照片"""
    start_page = 1
    end_page = 10000  # 可以修改这个值来获取更多或更少的页面
    all_photos = []  # 用于存储所有照片信息
    
    print(f"开始获取第 {start_page} 到 {end_page} 页的中国女性照片...")
    
    for page in range(start_page, end_page + 1):
        print(f"正在获取第 {page} 页...")
        data = get_photos(page)
        
        if data:
            photos = process_photos(data)
            all_photos.extend(photos)
            print(f"第 {page} 页获取完成，得到 {len(photos)} 张照片")
        else:
            print(f"第 {page} 页获取失败")
        
        # 在请求之间添加延迟，避免被封
        if page < end_page:
            delay = 2  # 秒
            print(f"等待 {delay} 秒后继续...")
            time.sleep(delay)
    
    print(f"总共下载了 {len(all_photos)} 张照片")

if __name__ == "__main__":
    main() 