import requests
import json

# 初始的category_id列表
category_id_list = [10515, 10516, 11207, 10742, 5914170, 11722, 11856, 5914132, 10518, 11578, 10523, 11859,
                    11863, 10586, 11723, 10521, 11304, 11714, 11128, 11720, 10519, 11670, 11627, 11669, 11443, 10522,
                    10527, 10517, 11307, 11320, 11291, 10530, 11529, 10531, 10520, 10532, 10525, 10529, 10524, 10526]

# URL和headers保持不变
url = "https://lv-api.ulikecam.com/artist/v1/effect/get_resources_by_category_id?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=1&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
    'charset': 'utf-8',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'content-type': 'application/json'
}

# 初始化一个空列表来存储所有的effect_item_list
all_effects = []

# 循环遍历每个category_id
for category_id in category_id_list:
    # 修改payload中的category_id
    payload = json.dumps({
        "app_id": 3704,
        "category_id": category_id,
        "category_key": "Winter",
        "count": 200,
        "filter_optional": {
            "filter_uncommercial": False,
            "no_copyrighted": False,
            "no_tuchong_order": False,
            "only_enterprise_commercial": False
        },
        "full_count": False,
        "offset": 100,
        "pack_optional": {
            "fav_scene": None,
            "image_pack_param": None,
            "large_image_formats": [],
            "need_collection_id": False,
            "need_contract": False,
            "need_favorite_info": True,
            "need_parent_tag": False,
            "need_tag": False,
            "need_thumb": False,
            "only_commercial": False
        },
        "panel": "default",
        "panel_source": "heycan",
        "replicate_sdk_version": "",
        "request_id": "",
        "statistics_optional": {
            "need_add_count": False,
            "need_favorite_count": False,
            "need_usage_count": False
        },
        "strategy_extra": ""
    })

    # 发送请求
    response = requests.request("POST", url, headers=headers, data=payload)
    # 解析响应
    response_data = response.json()
    # 提取effect_item_list并添加到all_effects列表中
    effect_items = response_data.get('data', {}).get('effect_item_list', [])
    all_effects.extend(effect_items)

# 将所有收集到的数据保存到一个JSON文件中
with open('all_effects.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'all_effects.json'. Total items collected: {len(all_effects)}")
