import requests as requests
import yaml

data = {
    "version": "3",
    "services": {
    }
}
# 获取代理
response = requests.get('https://dxycip.com/getOrderByToken?token=32e1239d4132b31109d43b06686c6d54')
proxy_data = response.json()# 尝试通过多个代理访问百度
proxy_list = proxy_data['data']
print(proxy_list)
for index, proxy_info in enumerate(proxy_list):
    proxy = proxy_info.split(' ')
    proxy_url = f"socks5://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
    data["services"][f"martian-server{index+1}"] = {
        "image": "zhaozuodong/gomitmproxy:latest",
        "restart": "always",
        "working_dir": "/go/src/gomitmproxy",
        "command": f"./gomitmproxy -v 1 -auth-username=\"cmm\" -auth-password=\"cmm123\" -downstream-proxy-url=\"{proxy_url}\" -use-local-ca-cert=true -kafka-topic=\"xhs-group\" -kafka-brokers=\"10.64.117.97:9092,10.64.117.98:9092,10.64.117.96:9092\" -allow-tls-urls=\"/api/sns/v3/user/info,/api/sns/v4/note/user/posted,/api/sns/v3/note/videofeed,/api/sns/v2/note/feed,/api/sns/v1/note/feed,/api/sns/v5/note/comment/list,/api/sns/v1/note/imagefeed,/api/sns/v4/note/videofeed\"",
        "ports": [
            f"{10001 + index}:8892"
        ]
    }
# 将 JSON 对象转换为 YAML 格式
yaml_data = yaml.dump(data, allow_unicode=True)

# 将 YAML 数据写入文件
with open('martian-server-compose.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml_file.write(yaml_data)

print("JSON 已成功转换为 YAML 文件")