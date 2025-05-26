import requests
import json

url = "https://lv-api-lf.ulikecam.com/artist/v1/effect/get_resources_by_category_id?channel=jianyingpro_0&version_name=7.0.0&opengl_version=3.0&aid=3704&effect_sdk_version=17.6.0&version_code=7.0.0&device_platform=mac&device_info={%22cpu%22:%22Apple%20M1%20Pro%22,%22gpu%22:%22Apple%20M1%20Pro%22,%22nv_driver_branch_version%22:%22%22,%22os_version%22:%2214.4.1%22,%22pc_gl_driver_version%22:%22%22,%22pc_gl_vendor%22:%22Apple%22,%22pc_gl_version%22:%223.0%22,%22version_code%22:%22458752%22}&region=CN&subdivision_id=&device_id=3340742688771322&gpu=Apple%20M1%20Pro&version_code_num=458752&biz_id=2&language=zh-Hans&cpu=Apple%20M1%20Pro&device_type=arm64"
headers = {
   'Host': 'lv-api-lf.ulikecam.com',
   'charset': 'utf-8',
   'x-ss-stub': 'a3d1fc2b1fcb5fe56e2a767b6071b661',
   'x-ss-dp': '3704',
   'x-tt-trace-id': '00-6b87f8700dbde6345400cfa8767b0e78-6b87f8700dbde634-01',
   'user-agent': 'Cronet/TTNetVersion:d4572e53 2024-06-12 QuicVersion:4bf243e0 2023-04-17',
   'x-helios': 'pVk6P2gdyQKRy1M6Cp4MMLDc+QgSPz1nN1pYXSirNByC524Y',
   'x-medusa': 'N4lGZ8NhGZ3jXppc4qOOF2NGJ3/oVgUCkU9bS9qpUBE4fRg+8XI9Ir1esgJS+7FV0TjI3Pd0j/3RmRyze1qcZe9vvHGjv3hspTip3VdpO3fCzJTJ78IcTFGazxFzepnc8JrP0O1CdTctDpR+CBFAcMLTSAgQE+T9BBOnhAgaMYCD2LIDF/c7/utOt6GuZDzMnPS43SA9Noot1Nf5ssje63LldFAiCezLiJtDsOth7emuO88HfLe644CB48Y/t692VpvmgQp3fGnPpN16WpBbKiubN75PDGjYsZWFMfkSsB+CLg2F/wwr27JJLY71UVwLSOYYOwNQgV8gMQOCt7MRKZnhjJBDfxWC0+isi9foZgi2/Eoh3EwSW+IT0q2JLNijo256wqn0hEfYHLsbYaCMoMJAF73zds3ZYZEunf9L8FHGdjJX5R6o8wOxQ1aYgaMPKosmHqiYYofm55nu+DMBRi6ndtpRPRfRmQ26qcewqmoJPD4Dpao2m1EsIkwnD6kbquTPhBck+2K0YEGJO71o9hU4BZ3uWnVVRvD4p/2O7C9ONEGkV5vol3UP72G0v3jRT9Oe9QAiosOnxGzBwRvFaQEnS9siWWA2b92I2Fj7QuTigw+B3BFlWTEy8ak3ZitalfcNNuIGZv0zetc+FvKZ5qNs9OUycjrRTZ6ZyIVXfjJqhVvnZ3G6lZ2Rd+lr49RcVAkH0Wp3XgarPBaOuV0A7oJOyvYX4SvqKWdCjDgSbdLfk7b4+zODG2ylJGaREweNEKvTVBM6RREZ7wDnPPz6NnO1lmEk+02f0n5e5mXznWyO92N4V/GtW8cY2yfBiNAuC01vSMRkGSZlO6TKKT6aLDjviv76fyDv8v8koH4=',
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
        "category_id": 7729,
        "category_key": "dream",
        "count": 50,
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
        "panel": "effects2",
        "panel_source": "loki",
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
with open('effect_atmosphere.json', 'w') as f:
    json.dump(all_effects, f, ensure_ascii=False, indent=4)

print(f"Data has been written to 'effect_atmosphere.json'. Total items collected: {len(all_effects)}")
