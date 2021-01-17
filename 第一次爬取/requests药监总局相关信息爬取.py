import requests
import json
if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    id_list = []  # 用来存储企业id
    all_data_list = []  # 存储所有的企业详情数据

    def is_json(file):
        try:
            json.loads(file)
        except Exception as e:
            return e
        return True
    # 网页url = 'http://scxk.nmpa.gov.cn:81/xk/'
    # 那网页数据  url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 具体内容请求 http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # data = {
    #     "on": "true",
    #     "page": 1,
    #     "pageSize": 1,
    #     "productName": '',
    #     "conditionType": 1,
    #     "applyname": '',
    #     "applysn": ''
    # }
    # page_num = requests.post(url=url, headers=headers,
    #                          data=data).json()['pageCount']
    for page in range(1, 50):
        data = {
            "on": "true",
            "page": page,
            "pageSize": 15,
            "productName": '',
            "conditionType": 1,
            "applyname": '',
            "applysn": ''
        }
        json_ids = requests.post(
            url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(
            url=post_url, headers=headers, data=data).json()
        all_data_list.append(detail_json)
    # 持久化存储
    fp = open('./第一次爬取/资源存放/allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('over')
