# -*- coding: UTF-8 -*-  

from aip import AipOcr

 
APP_ID = '你的APPID'
API_KEY = '你的API'
SECRET_KEY = '你的密钥'


aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

 
filePath = "C:\\Users\\Apple\\Desktop\\test.jpg"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}


result = aipOcr.webImage(get_file_content(filePath),options)

# url调用
# result = apiOcr.webImage('http://www.？？？？？.com/？？？？.jpg')

print(result)
