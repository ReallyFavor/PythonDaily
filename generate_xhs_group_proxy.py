import requests as requests

# 代理列表
proxy_list = [
    "182.151.20.5", "110.185.104.208", "182.151.59.206", "182.151.30.55", "110.188.23.182",
    "171.220.243.144", "182.151.47.125", "182.151.30.75", "182.151.0.47", "110.185.102.26",
    "182.151.21.42", "121.228.40.255", "114.218.57.150", "117.80.145.88", "117.80.86.226",
    "121.229.41.207", "58.209.83.182", "221.229.220.45", "180.101.23.151", "121.224.5.218",
    "117.80.86.233"
]

text = '''version: '3'
services:
'''
# 获取代理
for num in range(20):
    proxy_url = f"socks5://ty:ty@{proxy_list[num]}:7080"
    item = f'''
  martian-server{num+1}:
    image: zhaozuodong/gomitmproxy:latest
    restart: always
    working_dir: /go/src/gomitmproxy
    command: > 
      ./gomitmproxy -v 1
      -auth-username="cmm"
      -auth-password="cmm123"
      -downstream-proxy-url="{proxy_url}"
      -use-local-ca-cert=true
      -kafka-topic="xhs-group"
      -kafka-brokers="10.64.117.97:9092,10.64.117.98:9092,10.64.117.96:9092"
      -allow-tls-urls="/api/sns/v3/user/info,/api/sns/v4/note/user/posted,/api/sns/v3/note/videofeed,/api/sns/v2/note/feed,/api/sns/v1/note/feed,/api/sns/v5/note/comment/list,/api/sns/v1/note/imagefeed,/api/sns/v4/note/videofeed"
    ports:
      - "{10001 + num}:8892"
    '''
    text += item
with open('martian-server-compose.yaml', 'w', encoding='utf-8') as file:
    file.write(text)

print("YAML 配置已保存为 martian-server-compose.yaml")
