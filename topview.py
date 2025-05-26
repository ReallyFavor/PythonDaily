category_list = [
    {
        "categoryId": "5c2497374a3d4fc5920234865799892c",
        "categoryName": "General",
        "showNewBadge": 0
    },
    {
        "categoryId": "94be1b1967344af5b7734ea7511428bd",
        "categoryName": "Vitamins & Supplements",
        "showNewBadge": 0
    },
    {
        "categoryId": "980c4f010fef4f82872396175c292e98",
        "categoryName": "Medication",
        "showNewBadge": 0
    },
    {
        "categoryId": "2457489dc31d4c45b21a48c2796a6ced",
        "categoryName": "Beauty & Personal Care",
        "showNewBadge": 0
    },
    {
        "categoryId": "3287d33ee2a14791bce5538e6fea3558",
        "categoryName": "Fragrances",
        "showNewBadge": 0
    },
    {
        "categoryId": "f30e0cd3a3a84674992cdfbf5a38d3e4",
        "categoryName": "3C Digital Products",
        "showNewBadge": 0
    },
    {
        "categoryId": "d9d25e5c04e943ef9f33fc7625a28df9",
        "categoryName": "Beverages",
        "showNewBadge": 0
    },
    {
        "categoryId": "f937e35cf4ec423f9299fe1764d7fb2b",
        "categoryName": "Footwear",
        "showNewBadge": 0
    },
    {
        "categoryId": "e43e395d42e24d738280f98931a46150",
        "categoryName": "Drinkware",
        "showNewBadge": 0
    },
    {
        "categoryId": "442f928af5874777afa8af024f01b4c5",
        "categoryName": "Bags & Luggage",
        "showNewBadge": 0
    },
    {
        "categoryId": "6888b3af149b44d29c42b7603fa32e27",
        "categoryName": "Books",
        "showNewBadge": 0
    },
    {
        "categoryId": "112c544f36b9412ca9a56a1b07e1fe39",
        "categoryName": "Maternal & Infant Products",
        "showNewBadge": 0
    },
    {
        "categoryId": "a5517d937ed94fe5bc453ad59f333df8",
        "categoryName": "Large Appliances",
        "showNewBadge": 0
    },
    {
        "categoryId": "7d61b47d9bb64bb1a6cf945d1b185fef",
        "categoryName": "Food ",
        "showNewBadge": 0
    },
    {
        "categoryId": "3a4906cbeb744a98b388ba9867d6c22d",
        "categoryName": "Tools",
        "showNewBadge": 0
    },
    {
        "categoryId": "efd138ca09ae40489b58e9182e27a622",
        "categoryName": "Cycling Accessories",
        "showNewBadge": 0
    },
    {
        "categoryId": "72fbd7233f2d49be9c203dc902a12a72",
        "categoryName": "Kitchenware",
        "showNewBadge": 0
    },
    {
        "categoryId": "81696cc9fe434c08b13a42e82a7a6253",
        "categoryName": "App",
        "showNewBadge": 0
    },
    {
        "categoryId": "bd818b64510a4950b3243c7ab8d60e2d",
        "categoryName": "Watches",
        "showNewBadge": 0
    }
]

for category in category_list:
    print(category["categoryId"])

import subprocess
import json

# 构建 curl 命令
curl_command = [
    'curl',
    'https://www.topview.ai/api/trpc/productAvatar.getProductAvatarTemplateList?input=%7B%22pageSize%22%3A50%2C%22templateType%22%3A1%2C%22categoryIds%22%3A%2294be1b1967344af5b7734ea7511428bd%22%7D',
    '-H', 'accept: */*',
    '-H', 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    '-H', 'cache-control: no-cache',
    '-H', 'content-type: application/json',
    '-b', '__Host-next-auth.csrf-token=20d1da8e6d21a934fa0b25aa5c30521e039fe3fdd30afd1b0cd62816cf8bab99%7Ca5d2c56c879b5b5f59b774aa51cdb2320d637df87008873c99484dd39cc8987a; intercom-device-id-ks7obxbx=ad2972d3-893c-401e-a93c-9c5c58be4136; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.topview.ai%2Fgen%2Fproduct-avatar; subsType=free; intercom-session-ks7obxbx=VGdRZVBBSm82SnJTVlprUW1yaXB0L0pEN0NxK1lQUFNkL1FzN1VUQ3ZSZjFPcFgwSnhseWJFSWFWblpjMnFtaDlORDdSMVRUcnBxVXRDZHEvcnhmSGNKMjJURGhYcTdOb3FsY2EvT0Jrdm89LS0wc1VrQmllL29KSjk0ZmxDcExtZ053PT0=--f6c4d134162a3115b232a6850f31da852b5584a7; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..OfNs8slk5XCmc-Gz.irAfDcq5NlaXNpsbxHi02uf9o-ussXj8AzPfKZ7mXvn5d11jS6zmXbWdyHd4Xyft1se7nWxlEiwy4aTxa_LMHA7E_vSQD-M3l9bARmacSdOQ2lwAXkPkXF4yXc0lsxVTE97f6pVVd5XlqmtLMNw_9xlDsKhisDMzLtrFvO8Lm96Dum3mYGMAwmMgd6Ly3axBich0jx1EoFW9rqdW7mUSF3N_xt7ShMxRCrxBa4H71CCKY9noHRKnYJXF7ErTBrm2vFinpp1VcO5zEyYaT0PjJJHrDC94WO3x4yRsgwN6xCVYfK9sVyxCrlJMUN4XAMGr4qPZUle8ME1nmnY91MsMaVsC211Wpt2S0JN4NckWZretgPdkh1h_sfkPH-cSwT6aIphgJCFkwaSCOJE9s_hI6ZXAlGMiq0ei7ox-l-wRDObURrfprh5mj0_8SItAS69zTB0HNDwbLB65fF_KFZQA_iOVn9MDmJI1N0JbU7BNXa_T0a-o.MxGwvFuZBDeK3xH9D0CpUQ',
    '-H', 'pragma: no-cache',
    '-H', 'priority: u=1, i',
    '-H', 'referer: https://www.topview.ai/gen/product-avatar',
    '-H', 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
    '-H', 'sec-ch-ua-mobile: ?0',
    '-H', 'sec-ch-ua-platform: "macOS"',
    '-H', 'sec-fetch-dest: empty',
    '-H', 'sec-fetch-mode: cors',
    '-H', 'sec-fetch-site: same-origin',
    '-H', 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
]

# 执行 curl 命令
try:
    result = subprocess.run(curl_command, capture_output=True, text=True)
    if result.returncode == 0:
        print("响应内容：")
        # 解析 JSON 响应
        response_data = json.loads(result.stdout)
        
        # 提取数据
        if 'result' in response_data and 'data' in response_data['result']:
            data = response_data['result']['data']
            print("\n提取的数据：")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print("响应格式不符合预期")
            print(json.dumps(response_data, indent=2, ensure_ascii=False))
    else:
        print("错误：")
        print(result.stderr)
except json.JSONDecodeError as e:
    print(f"JSON 解析错误：{str(e)}")
    print("原始响应：")
    print(result.stdout)
except Exception as e:
    print(f"执行出错：{str(e)}")
