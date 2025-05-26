import requests
import json
import time
import os

# 创建保存图片的目录
if not os.path.exists('china_city_women_photos'):
    os.makedirs('china_city_women_photos')

# 设置请求头
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.pexels.com/search/china%20city%20woman/',
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
    '__cf_bm': 'T8ymtSEpUB.EtYOjtKd43DE4u0FMomzw7F_bOkI5kUs-1747907956-1.0.1.1-kbMFKKX_xJ4TiGEvkhKtb_nfJY2MW7pX61l9Yu5__P_AOGslsYDXJJ.NAXGBUHHnjg65UCaT8xwPZvfrtIk2lwF7HU.nPVI2FFjjk9iEb.s',
    '_sp_ses.9ec1': '*',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+May+22+2025+17%3A59%3A20+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=SG%3B&AwaitingReconsent=false',
    'cf_clearance': 'd9Q2LA.SceSVRdzO7dy2w0ne1PaBgdQcJ1nzSrNpy0M-1747907960-1.2.1.1-1CiClNc8au8oPktcpeuqlnMXOERKxjofzMD.npvmw5BwK9w8OIsWqCysBAv.0uEscOBr_Lgf2UJURTCoF47p5Tw7I7PHJDDxOOFcc6O51zz7YsLnK5hrz1nM1OPVuJJ_gvzuG7AeTs1ntGyZi5_E0_ZOdOqKuy2ZO3ihB9uSGmZBUa7D53ih5c4zXdc9f9UuLjl_T70QCjTirHKRPi54ZTbPsIgzFy4.olUpFhTra6mQQyV4At0Jd_4cYrEa0fuVIHYiRBaFUfbiV6_BFKBHZd4NJfd.XKf.x8uU0ed4KS6hy42X6QDE7VqvG.SRsxJHqaPqhexGJdar12c7t8awwhYyntVIRO2YWl2aO2HlI.E',
    '_sp_id.9ec1': 'e74076d9-f202-4980-b6ec-310e5bd1a192.1739176397.3.1747908112.1747882093.c748aacd-c6ea-44bb-b9ab-a74bb9443d8e.91845847-ecd3-4cc4-a20e-d2dfdbf2b95b.ef0dee87-8e49-4f97-9eed-f7279d76685b.1747907958883.21',
    '_pexels_session': 'lDWHVWC7PwadmXYM%2FFbsyPWDjmnRldpSZB50jSBGYd%2BblhGe6nef5RgKVV8TBOrkco%2B%2BXxqx0IIb%2BsuaoIxrzVFsvxelfRxrjeWuclz73%2FuF0P6kDp%2FEec9JODlpZxnn2oo71u3SK4Z88ZMhS%2Fav9t2xTLCYzBwKLLJrO52xSV%2BIZHniJwRNHrNiDX5l4vVVldsH8S%2F9%2BOXDDVoQDkJ0pe3dnLWMOKvi2MC%2F--avlrLf9Gc%2BTIWVSn--AEEYB6E4xImwNLXLr%2Fg9KA%3D%3D'
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
        "query": "china city woman",  # 修改为中国城市女性
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
                filename = f"china_city_women_photos/{photo_info['id']}.jpg"
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
    
    print(f"开始获取第 {start_page} 到 {end_page} 页的中国城市女性照片...")
    
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