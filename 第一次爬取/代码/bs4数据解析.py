# bs4进行数据解析
# - 数据解析原理：
#   - 1.标签定位
#   - 2.提取标签或标签属性中存储的数据值
# - bs4数据解析原理：
#   - 1.实例化一个beautifulSoup对象，并且将页面源码数据加载到该对象中
#   - 2.通过调用beautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
# - 环境安装：
#   - pip install bs4
#   - pip install lxml
from bs4 import BeautifulSoup
if __name__ == "__main__":
    # 将本地的 html 文档中的数据加载到该对象中
    fp = open('./第一次爬取/资源存放/html/fotoe.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup.meta)
    # print(soup.find('script'))
    print(soup.find_all('script'))