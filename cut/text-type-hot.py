import requests
import json

url = "https://lv-api-sinfonlinec.ulikecam.com/artist/v1/effect/get_resources_by_category_id?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
    "Host": "lv-api-sinfonlinec.ulikecam.com",
    "Cookie": "is_staff_user=false; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; HttpOnly; expires=Tue, 20-May-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; odin_tt=298be99c48217e8f6ffe7cd7f903fec52d7f11efb24afb4d421560107ca29c18dee5091dc4ee5a1eb249c63892c0422b72d236da108f9f3781a406cc0f6b669a605b4cd210b047427a5295736d6ef380; HttpOnly; expires=Tue, 20-Jan-2026 07:04:22 GMT; domain=.ulikecam.com; path=/; sessionid=23e5c70fc237c7505e29ed0590f1dcb4; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; sessionid_ss=23e5c70fc237c7505e29ed0590f1dcb4; secure; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; sid_guard=23e5c70fc237c7505e29ed0590f1dcb4%7C1737356662%7C5184000%7CFri%2C+21-Mar-2025+07%3A04%3A22+GMT; HttpOnly; expires=Thu, 15-Jan-2026 07:04:22 GMT; domain=.ulikecam.com; path=/; sid_tt=23e5c70fc237c7505e29ed0590f1dcb4; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; sid_ucp_v1=1.0.0-KDRiODNkYzczMjI0MWI3Yzg5NmVmOTViMjliYjQ1NzcyNzRlMTg3OGMKJwjM_eC1tfXyBBD26re8Bhj4HCAMKPqZgKq0zPcFMOrW1e0FOAhAJhoCbGYiIDIzZTVjNzBmYzIzN2M3NTA1ZTI5ZWQwNTkwZjFkY2I0; secure; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; ssid_ucp_v1=1.0.0-KDRiODNkYzczMjI0MWI3Yzg5NmVmOTViMjliYjQ1NzcyNzRlMTg3OGMKJwjM_eC1tfXyBBD26re8Bhj4HCAMKPqZgKq0zPcFMOrW1e0FOAhAJhoCbGYiIDIzZTVjNzBmYzIzN2M3NTA1ZTI5ZWQwNTkwZjFkY2I0; secure; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; store-region=cn-fj; HttpOnly; expires=Tue, 20-Jan-2026 07:04:22 GMT; domain=.ulikecam.com; path=/; store-region-src=uid; HttpOnly; expires=Tue, 20-Jan-2026 07:04:22 GMT; domain=.ulikecam.com; path=/; uid_tt=59b1f844a0fed84be88911158f3fb507; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; uid_tt_ss=59b1f844a0fed84be88911158f3fb507; secure; HttpOnly; expires=Fri, 21-Mar-2025 07:04:22 GMT; domain=.ulikecam.com; path=/; passport_csrf_token=1026f6db847f705d5b101400d2b912ff; secure; expires=Fri, 21-Mar-2025 07:01:12 GMT; domain=.ulikecam.com; path=/; passport_csrf_token_default=1026f6db847f705d5b101400d2b912ff; expires=Fri, 21-Mar-2025 07:01:12 GMT; domain=.ulikecam.com; path=/; passport_csrf_token_wap_state=c40eebdc3gAToVCgoVPZIGVlNGMwNjUwMWNiNWE5M2UzZTI3ZTA3ZWY4NmNiY2FloU6goVYBoUkAoUTTAAveY0VADPqhQdEOeKFNAKFIs2x2LWFwaS51bGlrZWNhbS5jb22hUgKiUEzRBCumQUNUSU9OoKFMoKFU2SBlZjBiOTY5YjkwNzA2OTUzOTZkMmU2ZjQ4NDM2NzY3N6FXAKFGAKJTQQChVcKiTUzC; secure; HttpOnly; expires=Mon, 20-Jan-2025 08:01:12 GMT; domain=.ulikecam.com; path=/;",
    "content-type": "application/json",
    "charset": "utf-8",
    "x-ss-stub": "9fefad0918cf545c768c4b264c241a36",
    "x-ss-dp": "3704",
    "x-tt-trace-id": "00-82899ab40dbde6345400cfa5b0de0e78-82899ab40dbde634-01",
    "user-agent": "Cronet/TTNetVersion:d4572e53 2024-06-12 QuicVersion:4bf243e0 2023-04-17",
    "x-helios": "anKIDSO9Vcg80YOnP1QroTLwh6HU6U/qf6PGBoKfpYE0YUoI",
    "x-medusa": "KPaNZ9we0p38IVFc/dxFF3w57H/JwgUCOj1bVVRYNQETXRiLOEMPi2c18gJUG2BF1/gd3fOUWv3fWYmzX7JAQeOnaellCkRc3tNB3XEJ7mfAJQBP76fuRV5SWhF3mkjM/loaIv4qxAcMjBR2byRSa07c6wE5hE37LpXdFOGZeBd1hUsch5LRHPrf8jpa64CXhpU6tkR/ZCQ8kpne0E2F1lnuepcgKP7n0hktfnIjohF19u+6RskVu99U36y3qSph2ZHGseBHJKJBqIlw0OHbPveS5JyA6ENEFkCTl4Wwf1YtDt0T2N8mhwYnLk/bGqIsncV+2vnHvTGoG6hANZIPY9oqxvLLNa/xXGirkU557t2RX0RdIKiuYSvdq92XyKfKIdPlZttCI1Am4D8Y8QMTDzet/L5lhTOaZ/Nf1jihnkQt8eKOsGoDluTqwuGMhSNoma0JzJqjDQNGp2QXlT1AFLfI7+1i1LLAElkFeKMdDJ/Syd65GitwBK7uHLsv1xQtLyBirrppVeiHJYt5EsVPwFPMVrW03G7duaoPByf8CQOkEQkKVzZkdrnjYDwMkYGjesPW6GqvVOW8Ux5gKOCXwtM8AeG1uVlNtzeyj35UMjUkt90jH6mclnzHI0U/0AmgPUb/9bzEAMKNtMUOSrIj0WbNLMO9JQO5r5LX4OZ1GeAJkz8c6Dx4sOx3cvPCapYTMnUCS3sy+H9YuZ4R6WyXMDNWKr2zXwCzN87f5dJYCBnWG8oaoLR4uKKAqT8xmY3r0lZC+bGtV5/RwZjujd2TpJq0fUgp3gY+iIcM+DvFLMlPLvgbRr8woIVMrzrz2H1OWSNZ0t27YQuPvwa4GPwnRfmfwf78n/Hv9B/xfHE="
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
        "category_id": 10577,
        "category_key": "10577",
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
    print(response_data)
    # 处理响应数据
    effects = response_data.get('data', {}).get('effect_item_list', [])
    all_effects.extend(effects)
    has_more = response_data.get('data', {}).get('has_more', False)

    # 递增offset
    offset += 200

# 将所有收集到的数据保存到一个JSON文件中
with open('text-type-hot.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'text-type-hot.json'. Total items collected: {len(all_effects)}")
