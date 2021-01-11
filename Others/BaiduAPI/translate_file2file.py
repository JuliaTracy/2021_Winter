import random
import hashlib
import urllib.parse
import json
import http.client
 
def baidu_translation(content):
    appid = ''  # 你的appid
    secretKey = ''  # 你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
 
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        # print(js)
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return (dst)  # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
 
# print(baidu_translation('My name is John.'))
english_data_list=[]
with open('C:\\Users\\Apple\\Desktop\\english_data.txt','r',encoding='utf-8') as f:
    for line in f:
        english_data_list.append(line.strip('\n'))
f.close()
# temp=''
# chinses_data_list=[]
# for line in english_data_list:
#     temp=baidu_translation(line)
#     print(temp)
#     chinses_data_list.append(temp)
 
with open('C:\\Users\\Apple\\Desktop\\chinese_data.txt','a+',encoding='utf-8') as f:
    for line in english_data_list:
        temp = baidu_translation(line)
        print(temp)
        # chinses_data_list.append(temp)
        f.write(temp+'\n')
f.close()
