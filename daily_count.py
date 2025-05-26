import requests
import json
url = "http://xhs-group-web.cmm-crawler-intranet-v2.k8s.limayao.com/basic-api/api/getDeviceList?sortedBy=did&sortedType=ascend&pageSize=50&currentPage=1&_t=1746001056903"

payload={}
headers = {
   'Accept': 'application/json, text/plain, */*',
   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
   'Authorization': 'h2hBbnLWjNGwfP3ySwAsWBnJxppUHUGro44jj4UE5aB',
   'Cache-Control': 'no-cache',
   'Connection': 'keep-alive',
   'Pragma': 'no-cache',
   'Referer': 'http://xhs-group-web.cmm-crawler-intranet-v2.k8s.limayao.com/',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
data = json.loads(response.text)

total_count = 0
for item in data['data']['devices']:
    if item['did'] <= 26:
        count = item['task_total_count']
        total_count += count

print(total_count)


# 钉钉机器人Webhook地址（包含access_token）
webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=5f0cdcab9734d032fe36e1a086eee50d78d9c069e3596980d8533c961e01580e'

# 消息内容
message = {
    "msgtype": "text",
    "text": {
        "content": f"截止到今日， 挂链评论总数为：{total_count}"
    }
}

# # 发送HTTP POST请求
# try:
#     response = requests.post(webhook_url, headers={'Content-Type': 'application/json'}, data=json.dumps(message))
#     if response.status_code == 200:
#         print("消息发送成功！")
#     else:
#         print(f"消息发送失败，状态码：{response.status_code}，响应内容：{response.text}")
# except Exception as e:
#     print(f"发送消息时发生错误：{e}")