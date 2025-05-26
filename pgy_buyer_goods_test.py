import time

import requests


def get_selection_center_list(cookie, group_id, page, size):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/feed'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://pgy.xiaohongshu.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "group_id": group_id,
        "size": size,
        "page": page,
        "cursor_score": "0",
        "source": 2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_item_detail(cookie, item_id, plan_id, seller_id):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/item/detail/basic'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "item_id": item_id,
        "plan_id": plan_id,
        "plan_type": 2,
        "seller_id": seller_id,
        "pack_scense": 2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_item_sku(cookie, item_id, plan_id, seller_id):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/item/detail/sku'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "item_id": item_id,
        "plan_id": plan_id,
        "seller_id": seller_id,
        "pack_scense": 3,
        "plan_type": 2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_seller_detail(cookie, item_id, plan_id, seller_id):
    url = f'https://pgy.xiaohongshu.com/api/draco/selection-center/item/detail/seller?item_id={item_id}&plan_id={plan_id}&seller_id={seller_id}&pack_scense=4'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_item_cooperation_data(cookie, item_id):
    url = f'https://pgy.xiaohongshu.com/api/draco/selection-center/item/detail/data?item_id={item_id}'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_sku_fulfillment_info(cookie, sku_id):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/sku_fulfillment_info'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "sku_id": sku_id
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_item_images(cookie, sku_ids):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/item/detail/images'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "sku_ids": sku_ids
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_seller_contact_info(cookie, seller_id):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/contact/info/query'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "source": "SELLER_CONTACT_INFO",
        "seller_id": seller_id,
        "source_page": "/microapp/selection/shop-detail"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_seller_item_list(cookie, seller_id, page, size):
    url = 'https://pgy.xiaohongshu.com/api/draco/selection-center/seller/detail/item/list'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'cookie': cookie
    }
    data = {
        "seller_id": seller_id,
        "page": page,
        "size": size,
        "order_by": {"field": "item_sales_qty", "asc": False},
        "is_hot": False
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def main():
    cookie = 'abRequestId=0c8c8c6b-ab09-5527-89ac-99687099fa5d; a1=18f03e8ab0bs823a0wid2c37e5sm6i5dmkchahu6i30000280219; webId=adf8c69b3b79044365e634c9fdd78d00; gid=yYi8qdY0iW6qyYi8qdY0DTx78DMYJq08E3fJSK3SqWd2Mxq86K32f0888JY8Jyj8ijijKKJ8; timestamp2=1716345254820b30a23faf137d2ef50b3ada114bbd1bbf4245d7a6f740de848; timestamp2.sig=LvXxChb-fwPGj-aTcYV2VGFeBFWEESL8ftR1qR5kE9Y; customerClientId=680930714100428; web_session=040069b405c832d1338b5614be344b1334d124; x-user-id-pro.xiaohongshu.com=65f94edfe200000000000001; x-user-id-creator.xiaohongshu.com=676bb79404ee000000000001; webBuild=4.55.1; unread={%22ub%22:%226785cd6600000000010091f9%22%2C%22ue%22:%2267a8a4e6000000001902f974%22%2C%22uc%22:34}; xsecappid=ratlin; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; customer-sso-sid=68c51747040194873320810637aacf99db3d0063; x-user-id-pgy.xiaohongshu.com=5e26c3eb000000000100b730; acw_tc=0a42136b17393384946256040ed3370cfc7b6c138e653963ec19688da35eef; solar.beaker.session.id=1739338494724056050077; access-token-pgy.xiaohongshu.com=customer.pgy.AT-68c517470401948730630403eskmtadbxs2oov15; access-token-pgy.beta.xiaohongshu.com=customer.pgy.AT-68c517470401948730630403eskmtadbxs2oov15'
    count = 0
    for page in range(1, 5001):
        group_id = 0  # Example group_id
        size = 10
        # Get selection center list
        selection_center_list = get_selection_center_list(cookie, group_id, page, size)
        # print("Selection Center List:", selection_center_list)
        for item in selection_center_list['data']['item_pack_elements']:
            item_id = item['itemInfo']['itemBasicInfo']['itemId']
            plan_id = item['planInfo']['planId']
            seller_id = item['sellerInfo']['sellerId']
            sku_id = item['itemInfo']['itemShowSkuInfo']['skuId']

            # Get item detail
            item_detail = get_item_detail(cookie, item_id, plan_id, seller_id)
            print("Item Detail:", item_detail)

            # Get item SKU
            item_sku = get_item_sku(cookie, item_id, plan_id, seller_id)
            # print("Item SKU:", item_sku)

            # Get seller detail
            seller_detail = get_seller_detail(cookie, item_id, plan_id, seller_id)
            # print("Seller Detail:", seller_detail)

            # Get item cooperation data
            item_cooperation_data = get_item_cooperation_data(cookie, item_id)
            # print("Item Cooperation Data:", item_cooperation_data)

            # Get SKU fulfillment info
            sku_fulfillment_info = get_sku_fulfillment_info(cookie, sku_id)
            # print("SKU Fulfillment Info:", sku_fulfillment_info)

            # Get item images
            item_images = get_item_images(cookie, [sku_id])
            # print("Item Images:", item_images)

            # Get seller contact info
            seller_contact_info = get_seller_contact_info(cookie, seller_id)
            print("Seller Contact Info:", seller_contact_info)

            # Get seller item list
            seller_item_list = get_seller_item_list(cookie, seller_id, page, size)
            print("Seller Item List:", seller_item_list)
            count += 1
            print(count, "----------------------------" * 10)
            time.sleep(3)


if __name__ == "__main__":
    main()
