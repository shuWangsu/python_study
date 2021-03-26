bs4进行数据解析
    - 数据解析原理：
        - 1.标签定位
        - 2.提取标签或标签属性中存储的数据值
    - bs4数据解析原理：
        - 1.实例化一个beautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用beautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装：
        - pip install bs4
        - pip install lxml
    - 如何实例化一个 beautifulSoup 对象：
        - from bs4 import BeautifulSoup
        - 对象的实例化：
            - 1.将本地的html文档中的数据加载到该对象中
                fp = open('./xxx.html', 'r', encoding='utf-8')
                soup = BeautifulSoup(fp,'lxml')
            - 2.将互联网上获取的页面源码加载到该对象中
                response = requests.get(url=url, headers=headers).text
                soup = BeautifulSoup(response,'lxml')
        - 提供的用于数据解析的方法和属性：
            - 1. soup.tagName 返回的是html中第一次出现的tagName标签
            - 2. soup.find():
                - find('tagName'):等同于 soup.tagName
                - 属性定位：
                    -find('tagName', class_/id/attr="xxx")
            - 3. soup.find_all('tagName'): 返回符合要求的所有标签（返回的是列表）
            - 4. soup.select():
                - select('某种选择器(类，ID，标签选择器)'), 返回的是一个列表
                - 层级选择器：
                    - select('.className > ul > li > a') : > 表示的是**一个层级**。返回的是一个列表
                    - select('.className > ul a') : ul与 a之间的 空格 表示的是**多个层级**。返回的是一个列表
            - 5. 获取标签之间的文本数据：
                - soup.tagName.text/string/get_text()
                - text/get_text(): 可以获取某一标签中的所以文本内容（不是直系也可以）
                - string: 只可以获取该标签下的直系的文本内容
            - 6. 获取标签中属性值：
                - soup.tagName['属性名']

