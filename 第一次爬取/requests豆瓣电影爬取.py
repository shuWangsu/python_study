#需求：豆瓣电影爬取
  # ——post请求
  # ——响应数据是一组json数据

import requests
import json
if __name__ == "__main__":
  #UA伪装：将对应的User-Agent封装到一个字典中
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  }
  url = 'https://movie.douban.com/j/chart/top_list'
  param = {
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':'0',  #从库中第几部电影去取
    'limit':'50'  #一次取出的个数
  }
  response = requests.get(url=url, params=param,headers=headers)
  list_data = response.json()
  fp = open('./douban.json', 'w', encoding='utf-8')
  json.dump(list_data, fp=fp, ensure_ascii=False)
  print('over')