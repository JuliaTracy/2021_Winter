import json
from urllib.request import urlopen,quote
import requests

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoding/v3/?address='
    output = 'json'
    ak = 'CAuOEMMNyxoKzRIFTmNwwX918zdARAvl' 
    #通过百度创建应用得到ak，记得写为浏览器端，然后写*
    address = quote(address)
    uri = url+address+'&output='+output+"&ak="+ak
    req = urlopen(uri)
    res = req.read().decode()
    #print(res)
    temp = json.loads(res)
    
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat,lng
'''lat0=[]
lng0=[]
#filename="C:\\Users\\Apple\\Desktop\\北京.txt"
#with open(filename,'w') as f:
place = ["铜仁市","襄阳市","海东市","那曲市","林芝市","山南市","日喀则市"]
for loc in place:
    lat,lng = getlnglat(loc)
    lat0.append(lat)
    lng0.append(lng)
        #f.write("%s %f %f\n"%(loc,lng,lat))
for i in range(0,len(place)):
    print("\""+place[i]+'_1.txt\", ',end='')
    print("\""+place[i]+'_2.txt\", ',end='')
    print("\""+place[i]+'_3.txt\", ',end='')
    print("\""+place[i]+'_5.txt\", ',end='')
    print("\""+place[i]+'_10.txt\", ',end='')
for i in range(0,len(lng0)):
    print("%.2f, "%(lat0[i]),end='')
print('\n')
for i in range(0,len(lat0)):
    print("%.2f, "%(lng0[i]),end='')'''
lat,lng=getlnglat("上海朱家角污水处理工程建设有限公司")
print(lat)
print(lng)

        
