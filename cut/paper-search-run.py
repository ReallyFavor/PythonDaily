import requests
import json

url = "https://lv-api-sinfonlinec.ulikecam.com/artist/v1/effect/search?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"

headers = {
    'Host': 'lv-api-sinfonlinec.ulikecam.com',
    'content-type': 'application/json',
    'charset': 'utf-8',
    'x-ss-stub': '00932f205d34a1bde4c2f05e26d26f96',
    'x-ss-dp': '3704',
    'x-tt-trace-id': '00-687f289a0dbde6345400cfae86a90e78-687f289a0dbde634-01',
    'user-agent': 'Cronet/TTNetVersion:d4572e53 2024-06-12 QuicVersion:4bf243e0 2023-04-17',
    'x-helios': 'wLv2DuRH2x52iwwpJ8fyfmI14wm/Jrrfe0GZtsn+Lb3cr2t2',
    'x-medusa': 'jEuHZ3ij2J1YnFtcWWFPF9iE5n/TrAUCgdhbYVqPTREAfVgklHqYtzB9xgNSI4RF0+C93fesuv3bYSmzeIIu8euWgm7KONv5KBvd3VU/j1bKv+Bt4hYD9RTld/z8H4/9HeU7eRIo+OPFX95FY6lJEHxecIlx0N3BvYVlwwTLK+DaUS2w4Ge2DbgMx/KJGgwWy6Tq6vfZiCyekmpEz9gWvnyG+extIl2f0Q+ugTfOxPjdT53xqEM+Qv2pQ69EkFJeuvISHddH+JT63Bh9RyYS7aELJ1JE3+Ciy/M5QWCO+XAZ34+zq9m8gCrLkNboNV3Q2lvFCZE4xQkZ1m3CnvnRM5EKYU0q/9e3/5QVAlrHxJ8gOqEtS0N5JeSu5z8t4NCxRkLfjNgGnhrenvkqV4h7F4ytd6tOthwBgqQVVqlf/GK+1f9+o3iSxf/t9nzAqhgqz0SQXWT81EcqeeACxlAscD/E6grAtt/9rl1oXzrGZqoxoK3IbDO87wnBFK2qztpsHeu/W7txYphKgHsjSLpv++o8mYOtDjQkl+6dGRqnJzZKXzsyBqBx/VoiPffulIhoH2BdCRIK7ElrFIkX5Qv6sV0S7ynh6nZQmQpnEUtOvE9vPRUGxf1kCgmbgNRc8unicndy3wrRAnCMOYCiwbt/a7iiYeDR9OaQ4vZ4lvPtBxHmO6e+kBymOr+BW6RVTphX0Oo2I97XXCZpKS4V8NkkiMIN0nnsBQktDA2YHINjDstDoDmOcQ9iKpypknbPb4Z+KQCvmOhZ1BtMrgcI81g4MhEQ262dQt6lYmvnFhdhqH45/Ey9QkBzVSZtQg/Kyww2XsqbR2LmB3upDGK7Ska0+0+CE/76pxXv+AcR+xI='
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
        "count": 50,  # 根据curl命令修改为50
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
        "query": "跑",  # 修改搜索关键词
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
    offset += 50  # 根据count值修改步进值

# 将所有收集到的数据保存到一个JSON文件中
with open('paper-search-run.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"数据已写入 'paper-search-run.json' 文件。总共收集的项目数: {len(all_effects)}") 