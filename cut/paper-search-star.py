import json

import requests

url = "https://lv-api-lf.ulikecam.com/artist/v1/effect/search?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
    'Host': 'lv-api-lf.ulikecam.com',
    'charset': 'utf-8',
    'x-ss-stub': '22511f701a6113f661940239da49272f',
    'x-ss-dp': '3704',
    'x-tt-trace-id': '00-8a9bff5f0dbde6345400cfa492bb0e78-8a9bff5f0dbde634-01',
    'user-agent': 'Cronet/TTNetVersion:d4572e53 2024-06-12 QuicVersion:4bf243e0 2023-04-17',
    'x-helios': 'OBWdTAy6uGqICexoVjKnIdKh8VtZDy7E8gBLPdOMMm3tnKqN',
    'x-medusa': '8H1OZwSVEZ0kqpJcJVeGF6SyL3+cmAUCIkpbZEvhexELfRiLPTPWm2BlawJTa71V2IjE3PTkh/3YKRAyWUIU5+jaP09H2BLzQe0MJntCl3bDXXhKx9UczGjkDTSc5Sl3SeXE25kFlqlEsrmV7Q0mrGBLTVhxTGJnfpoWVT8BQfBR22NXvnrFCIn0Qc/iHnfPBLCygEAiJAcCG1b380zyUwk53wTbXTj8XjSlUdRm2Y7ltLqB8W58Ne4dwwSke6K6rk/K7nlV7pDdEjYu6hB4dGmsvXDLqnvu8q9azQnnIhIigBbor7niXkHxIbR3ILGJCseYqjzDZX+m7wdN5debqN/66aKxdmtDh6EkbPzjotG26feHpF1Qm9E/wEmh+l2yMV9uCvLDmjKkfHf6IT1TWgvJ1nD6kM9Vyle5L3b1th8XbQs5AQHfWl5/cM8PlQ0x8V0QQvtLKHQv8MnysSVOmMhzttnknEuMFWN99cOef9p4vU6uBNr+vxA2iU/Whex855tX35WEPLxQ/wyqGgPOqA77zRciV47KUO16lurYZBbZ6foMBSMzps3IsfmyNv2fsMcnr33dPcpPw865BDiGrT5vATDCYjP3Afd1M3dTpAOgIe2k77zlQlGejnCn8iRr6e15wOS9YNN2kzO9ZsxOiN/FW7eH7ob1Oe8GIzM3RiGq1nGeh93wQa3ZdW1aaUgwnxfg8l0rQmvMqJ6W5Xpw3pS1G/atDuNLvSE9XRAllJs50XIXroICFFuPmfmN9BGasYp7HXZo8x+CGl7zQh4/l1zHYqptbVewDOMrWFGBxXgWVMmj+Ss6kC/gllUEpcn7j7NMNbhlspA9beT8Ypnwv6jUjf/77yj/808okkE=',
    'content-type': 'application/json'
}

# 初始化offset
offset = 0
has_more = True

# 存储所有结果的列表
all_effects = []

while has_more:
    # 更新payload中的offset
    payload = json.dumps({
        "app_id": 3704,
        "count": 200,
        "effect_type": 2,
        "need_recommend": False,
        "offset": offset,
        "pack_optional": {
            "fav_scene": None,
            "image_pack_param": None,
            "large_image_formats": [],
            "need_collection_id": False,
            "need_contract": True,
            "need_favorite_info": False,
            "need_parent_tag": False,
            "need_tag": False,
            "need_thumb": False,
            "only_commercial": False
        },
        "query": "星星",
        "replicate_sdk_version": "",
        "search_id": "",
        "search_option": {
            "aspect_ratio": "",
            "filter_uncommercial": False,
            "scene": "",
            "sticker_type": 0
        },
        "statistics_optional": {
            "need_add_count": False,
            "need_favorite_count": False,
            "need_usage_count": False
        }
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()

    # 处理响应数据
    effects = response_data.get('data', {}).get('effect_item_list', [])
    all_effects.extend(effects)
    has_more = response_data.get('data', {}).get('has_more', False)

    # 递增offset
    offset += 200

# 将所有收集到的数据保存到一个JSON文件中
with open('star.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'all_effects.json'. Total items collected: {len(all_effects)}")
