import requests
import re
import os
import json
if __name__ == "__main__":
    if not os.path.exists('./第一次爬取/资源存放/image/fotoeLibs'):
        os.mkdir('./第一次爬取/资源存放/image/fotoeLibs')
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    url = 'http://www.fotoe.com/publication/23297'

    # http://www.fotoe.com/thumbnail/11841441
    #爬取整张页面
    response = requests.get(url=url, headers=headers)
    # 获取响应数据
    page_text = response.text
    ex = '<div class="image_group">.*?<img src="(.*?)" alt.*?></div>'
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        # src = src.replace(str[0],'')
        src = 'http://www.fotoe.com' + src.replace('.','')
        img_data = requests.get(url=src, headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]
        #存储图片路径
        img_path = './第一次爬取/资源存放/image/fotoeLibs/' + img_name + '.jpg'
        # 持久化存储
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name + '.jpg 下载完成！') 
