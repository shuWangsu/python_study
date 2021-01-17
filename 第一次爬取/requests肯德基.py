#需求：肯德基门店数据爬取
  # ——post请求
  # ——响应数据是一组json数据

import requests
import json
if __name__ == "__main__":
  #UA伪装：将对应的User-Agent封装到一个字典中
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  }
  url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
  keyword = input('输入地点：')
  param = {
    "cname": '',
    "pid": '',
    "keyword": keyword,
    "pageIndex": 1,
    "pageSize": 10
  }
  response = requests.post(url=url, params=param,headers=headers)
  table_data = json.loads(response.text)
  fp = open('./第一次爬取/资源存放/'+ keyword + '.json', 'w', encoding='utf-8')
  json.dump(table_data, fp=fp, ensure_ascii=False)
  print('over')