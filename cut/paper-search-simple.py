import requests
import json

url = "https://lv-api-lf.ulikecam.com/artist/v1/effect/search?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
    'charset': 'utf-8',
    'x-ss-stub': '38b8d317b8f6a43c6cd03a57a01c7cf9',
    'x-ss-dp': '3704',
    'x-tt-trace-id': '00-249095230dbde6345400cfa3eac90e78-249095230dbde634-01',
    'x-helios': '4SRVObLtiORfSTjGohddyqKHB3Y6DL7GkTUzVAKq/y5+5chJ',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
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
        "query": "简约",
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
with open('simple.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'all_effects.json'. Total items collected: {len(all_effects)}")
