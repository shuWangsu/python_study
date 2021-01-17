#需求：破解百度翻译
  # ——post请求
  # ——响应数据是一组json数据

import requests
import json
if __name__ == "__main__":
  #UA伪装：将对应的User-Agent封装到一个字典中
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  }
  post_url = 'https://fanyi.baidu.com/sug'
  kw = input('输入词条：')
  data = {
    'kw': kw
  }
  response = requests.post(url=post_url, data=data, headers=headers)
  #获取响应数据：json() 方法返回的是 obj (如果确定响应数据是json类型的，才可以使用json())
  dic_obj = response.json()
  #持久化存储
  filePath = './第一次爬取/资源存放/'+ kw +'.json'
  fp = open(filePath , 'w', encoding='utf-8')
  json.dump(dic_obj, fp=fp,ensure_ascii=False)
  print('over')