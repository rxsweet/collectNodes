import re
import os
import requests
from datetime import datetime   #时间


def getContent(url):#获取网站的内容，将获取的内容返回
    headers = {'User-Agent': 'Opera/9.25 (Windows NT 5.1; U; en)'}

    try:
        r=requests.get(url,headers=headers)
        print(r)
        if r.status_code==200:
            r.encoding='utf-8'    #编码方式
            groups = re.findall(f'href="((https://www.85la.com/\d{4}/.html)"(.*?)/{y}/{m}/', content, flags=re.I)
            print(groups)
            return r.text
    except requests.exceptions.RequestException as e:  
        #print(e)
        #print('getContent()功能中出现的错误！获取内容失败，或者打开网址错误!')
        print(f'获取{url}内容时出错')
        return []






if "__name__==__main__":#主程序开始的地方
    getContent("https://www.85la.com/")
