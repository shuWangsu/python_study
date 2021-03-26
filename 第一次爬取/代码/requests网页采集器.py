#UA:User-Agent (请求载体的身份标识)
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，
  #如果检测到请求的载体身份标识为某一款浏览器，说明是正常请求。
  #但是，如果检测到请求的载体身份标识不是基于某款浏览器的，则表示为不正常请求（爬虫）
  #则服务器端就很可能拒绝请求
#UA伪装：让爬虫对应的请求载体身份标识伪装为某一款浏览器

import requests
if __name__ == "__main__":
  #UA伪装：将对应的User-Agent封装到一个字典中
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
  }
  url='https://www.sogou.com/web'
  #处理url携带的参数:封装到字典中
  keyword = input('输入一个词:')
  param = {
    'query': keyword
  }
  #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
  response = requests.get(url=url,params=param, headers=headers)
  page_text = response.text
  fileName = keyword + '.html'
  with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
  print(fileName,'保存成功')

