Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> kv = {'wd' :'Python'}
>>> r=requests.get("http://www.baidu.com/s",params=kv)
>>> r.request.url
'http://www.baidu.com/s?wd=Python'
>>> r.status_code
200
>>> len(r.text)
618155
>>> 