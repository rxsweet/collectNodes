import os
import requests
import urllib.parse
from datetime import datetime

#clash文件地址

#默认转clash配置文件.ini地址
INI_CONFIG = 'https://raw.githubusercontent.com/rxsweet/all/main/githubTools/clashConfig.ini'

# 使用远程订阅转换服务，输出相应配置,默认输出clash订阅格式
# 注意 订阅地址必须是base64,或者yaml，(直接是url节点内容的话，会解析错误)
def convert_remote(url='', output_type='clash',configUrl = INI_CONFIG):
    #url='订阅链接', 
    #output_type={'clash': 输出可以订阅的Clash配置, 'base64': 输出 Base64 配置, 'url': 输出 url 配置, 'YAML': 输出 YAML 配置}, 
    #host='远程订阅转化服务地址',configUrl转clash订阅时用
    #host='http://127.0.0.1:25500'
    #sever_host = host
    sever_host = 'http://127.0.0.1:25500'
    url = urllib.parse.quote(url, safe='') # https://docs.python.org/zh-cn/3/library/urllib.parse.html
    if output_type == 'clash':
        converted_url = sever_host+'/sub?target=clash&url='+url+'&insert=false&config='+configUrl+'&emoji=false&append_info=true'
        try:
            resp = requests.get(converted_url)
            print(resp)
        except Exception as err:
            print(err)
            return 'Url 解析错误'
        if resp.text == 'No nodes were found!':
            sub_content = 'Url 解析错误'
            print('Url 解析错误: No nodes were found! -->' + url + '\n')
        else:
            sub_content = resp.text
    elif output_type == 'base64':
        converted_url = sever_host+'/sub?target=mixed&url='+url+'&insert=false&emoji=false'
        try:
            resp = requests.get(converted_url)
        except Exception as err:
            print(err)
            return 'Url 解析错误'
        if resp.text == 'No nodes were found!':
            sub_content = 'Url 解析错误'
            print('Url 解析错误: No nodes were found! -->' + url + '\n')
        else:
            sub_content = resp.text
    elif output_type == 'url':
        converted_url = sever_host+'/sub?target=mixed&url='+url+'&insert=false&emoji=false&list=true'
        try:
            resp = requests.get(converted_url)
        except Exception as err:
            print(err)
            return 'Url 解析错误'
        if resp.text == 'No nodes were found!':
            sub_content = 'Url 解析错误'
            print('Url 解析错误: No nodes were found! -->' + url + '\n')
        else:
            sub_content = resp.text
    elif output_type == 'YAML':
        converted_url = sever_host+'/sub?&target=clash&url='+url+'&emoji=false&append_type=false&append_info=true&scv=false&udp=false&list=true&sort=false&fdn=true&insert=false'
        try:
            resp = requests.get(converted_url)
        except Exception as err:
            print(err)
            return 'Url 解析错误'
        if resp.text == 'No nodes were found!':
            sub_content = 'Url 解析错误'
            print('Url 解析错误: No nodes were found! -->' + url + '\n')
        else:
            sub_content = resp.text
    return sub_content

#源文件转到目标文件，类型为output_type，共4个类型：clash,base64,url,YAML
def fileToFile(source,output_type,output):

    time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{time}]: subconvert [{output_type}]- [{source}] to [{output}]')
    #获取文件绝对路径
    source_path = os.path.abspath(source)
    temp = convert_remote(source_path,output_type)
    with open(output, 'w') as f:
        f.write(temp)



if __name__=='__main__':
    #获取参数携带的参数
    args = sys.argv
    if args:
        source = args[0]
        output_type = args[1]
        output = args[2]
        fileToFile(source,output_type,output)
