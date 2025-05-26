import requests as requests
proxy_list = [
    # "182.151.20.5", "110.185.104.208", "182.151.59.206", "182.151.30.55", "110.188.23.182",
    # "171.220.243.144", "182.151.47.125", "182.151.30.75", "182.151.0.47", "110.185.102.26",
    # "182.151.21.42", "121.228.40.255", "114.218.57.150", "117.80.145.88", "117.80.86.226",
    # "121.229.41.207", "58.209.83.182", "221.229.220.45", "180.101.23.151", "121.224.5.218",
    # "117.80.86.233"
    "124.225.86.236",
]
for num in range(len(proxy_list)):
    proxy_url = f"socks5://ty:ty@{proxy_list[num]}:7080"
    print(proxy_url)
    # 设置代理
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    try:
        response = requests.get("http://www.baidu.com", proxies=proxies, timeout=5)
        print(f"使用代理 {proxy_url} 访问成功")
        # print(response.text)
        # break  # 成功后退出循环
    except requests.exceptions.RequestException as e:
        print(f"使用代理 {proxy_url} 访问失败: {e}")
