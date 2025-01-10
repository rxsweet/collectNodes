import re
import os
import requests
from datetime import datetime   #时间


def getContent(url):#获取网站的内容，将获取的内容返回
    headers={"user-agent": "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/73.0.3683.121 MZBrowser/9.12.1 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
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
    getContent("http://www.85la.com/")
