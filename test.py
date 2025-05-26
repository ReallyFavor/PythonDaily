import requests
import json

for num in range(0,10):
    proxy_url = f"socks5://{num}:cmm@10.66.8.2:8083"
    print(f"\n测试代理: {proxy_url}")
    # 设置代理
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    try:
        # 使用 ipinfo.io 服务获取IP信息
        response = requests.get("https://ipinfo.io/json", proxies=proxies, timeout=5)
        ip_info = response.json()
        
        print(f"IP地址: {ip_info.get('ip', '未知')}")
        print(f"位置: {ip_info.get('city', '未知')}, {ip_info.get('region', '未知')}, {ip_info.get('country', '未知')}")
        print(f"ISP: {ip_info.get('org', '未知')}")
        
    except requests.exceptions.RequestException as e:
        print(f"访问失败: {e}")
    except json.JSONDecodeError as e:
        print(f"解析响应失败: {e}")
