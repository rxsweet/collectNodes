import os
import requests
import urllib.parse

#clash文件地址
FILE_PATH = './subs/mining.yaml'
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
        converted_url = sever_host+'/sub?target=clash&url='+url+'&insert=false&config='+configUrl+'&emoji=false'
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
            sub_content = sub_convert.base64_encode(resp.text)
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
    return sub_content





if __name__=='__main__':
    #获取allyaml_path文件路径
    f_path = os.path.abspath(FILE_PATH)
    clash = convert_remote(f_path,'clash')
    with open('./subs/1.yaml', 'w') as f:
        f.write(clash)
    v2ray = convert_remote(f_path,'base64')
    with open('./subs/1.txt', 'w') as f:
        f.write(clash)
