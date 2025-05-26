import os,requests,time

from groq import Groq


types = [
    "日用百货",
    "鲜花园艺",
    "食品饮料",
    "钟表首饰",
    "运动户外",
    "艺术收藏",
    "母婴儿童",
    "服饰鞋包",
    "个护美体",
    "旅游住宿",
    "文化娱乐",
    "数码家电",
    "彩妆护肤",
    "家居家装",
    "宠物生活",
    "医疗健康",
    "汽车",
    "其他"
]
def get_names_no_type(num):
    # url = "http://dy-ad-web.cmm-crawler-intranet.k8s.limayao.com/api/getKw?proc=1"
    url = "http://dy-ad-web.cmm-crawler-intranet.k8s.limayao.com/api/getKw"
    payload = {}
    headers = {}

    namesNoType = []
    while len(namesNoType) < num:
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        name = data["kw"]
        if name not in namesNoType:
            namesNoType.append(name)
        time.sleep(0.1)
    print(len(namesNoType))
    question_str = str(namesNoType) + ",给这个数组里的名称分类,只能从以下类别中选择:" + str(
        types) + '''.直接返回结果数组,不要其他回答.如[{"key":"酸菜鱼","value":"食品饮料"}]'''
    print(question_str)
    return question_str


question_str = get_names_no_type(150)

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question_str,
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)