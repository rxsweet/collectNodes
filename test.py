import os
import requests


PATH = os.path.abspath(os.path.dirname(__file__))  # 1.os.path.dirname(_file_) 返回脚本的绝对路径.. 2.可嵌套使用，如 os.path.dirname(os.path.dirname(path) ) 返回父路径的父路径,,https://blog.csdn.net/qq_43404784/article/details/88994350
print(PATH)
#http://localhost:25500/sub
res=requests.get('http://localhost:25500/',timeout=5)#设置5秒超时防止卡死
if res.status_code == 200:
    res.encoding='utf-8'
    print(res.text)
