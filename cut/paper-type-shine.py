import requests
import json

url = "https://lv-api-sinfonlinec.ulikecam.com/artist/v1/effect/get_resources_by_category_id?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
   'Host': 'lv-api-sinfonlinec.ulikecam.com',
   'charset': 'utf-8',
   'x-ss-stub': '6d2d42e41b830daae57d563621ebb7b2',
   'x-ss-dp': '3704',
   'x-tt-trace-id': '00-687875f80dbde6345400cfa4a8200e78-687875f80dbde634-01',
   'user-agent': 'Cronet/TTNetVersion:d4572e53 2024-06-12 QuicVersion:4bf243e0 2023-04-17',
   'x-helios': 'V8whMUXYMcHnn089XclKdsVgYSrFTf/sSJ0YEPKB4inozx2K',
   'x-medusa': '20mHZy+h2J0PnltcDmNPF4+G5n/WtQUCvOMb1fU1FgE6XVhwG3EijCxI4QJXGyZF1lhb3PCUHP3W2c+zfTqM4eYOJDpFM2XSPA663FIHLVbHJwZs5S6h9Rl90fz5JyntGH2dOODMxrbZ3x+35+K3FIriN68/3YkIQ5MBxpbuyD/BAPYkOCBXP3dHYNE2RHEGU4Ym+5hLBLan/RwBKmA1zsgSqtSF7e4lHs36UqNZpSY3iUVtQn4zeTNek8GSojbyd1y/sGBfCZwbT6VA2Z8bH+cMgo2vaDvLAEB8GbzIqBZ7eMsuWi3SxdpTfMl7u8sY/riq2dFiI5PBSNBmTNHqhP5EOJigDhYGI0UydgtWyAnCvnieCMVd4xQuxmnoalc//burU7p5f3faUJLxPOi+WnjpJdKN+ckxL4lWmOWGOxw2crfH4qF5XBSpp0g6JzvPDUhPFhfqyh/XsAICDV2Zm3y1tI19lmQmdYXa23by33zaJ1QQ3e9JimRwLsSqIeqlU/CP4i8K46JCRsqrGO5Zbv23VxM2Hg6ADl/SjxbN/hGFZyhiFQQcUtMrOSyiT7HjWoJYEpHuUwqZ6s6XzxUZoIG51EoDOQWF2uK1x9pxy2fZ9Wu1Kcc5XX3oRUujpfwcASl8rtUjs61MsmPaJsu2+igdchVcOUhC0IL7VZ+ldJlmaU4MGGZhXQGVZ+QUwL3hWI8V1KcFCmWSknMpIvQJZLUY/P5hqJeHNpQFNmWC8xCiPVjJbcK481B4GNptM/VumRWzoWd4oUs3mgawgXHALCY/OzNzqN8HjcXaiHHLAnTzYYThT9lLSjLMsTKVgILlHC8ikNRLpMpXPNkezbl+Xp08K//9H7Pv/Z+3TAY=',
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
        "category_id": 10520,
        "category_key": "10520",
        "count": 200,
        "filter_optional": {
            "filter_uncommercial": False,
            "no_copyrighted": False,
            "no_tuchong_order": False,
            "only_enterprise_commercial": False
        },
        "full_count": False,
        "offset": 0,
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
with open('paper-search-shine.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'paper-search-shine.json'. Total items collected: {len(all_effects)}")
