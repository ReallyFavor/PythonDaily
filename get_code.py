from datetime import datetime

import requests
from bs4 import BeautifulSoup

phone_list = ["15517905537", "13233983107", "18659242036", "17537978911", "18574005398",
              "18639271500", "17644495135", "17537992511", "18568336069", "17518895731"]

phone_list = ["13213696025", "15517972059", "15517930550", "13233917672", "15517927670", "13233922317", "17638813571"]

for phone in phone_list:
    res = requests.get(f"http://192.168.23.23:6789/content?phone={phone}")
    # 解析HTML
    soup = BeautifulSoup(res.text, 'html.parser')

    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')

    # 查找所有的<a>标签
    items = soup.find_all('a', class_='list-group-item')

    # 查找所有的<a>标签
    items = soup.find_all('a', class_='list-group-item')

    for item in items:
        # 提取日期
        date_text = item.find('small').text.strip()
        date = date_text.split(' ')[0]

        # 检查日期是否为今天
        if date == current_date:
            try:
                # 提取验证码
                p_text = item.find('p').text
                code_start = p_text.find('验证码是: ') + len('验证码是: ')
                code_end = p_text.find('，', code_start)
                code = p_text[code_start:code_end]
                print(f"{phone} verification code is: {code}")
            except:
                pass
