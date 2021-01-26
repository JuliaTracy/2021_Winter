months = []
#for year in (2019,2020):
year=2020
for month in range(12):
    months.append("%d%02d"%(year, month+1))
todo_urls=[]
print(months)
for i in range(0,len(months)):
    todo_urls.append(
        f"http://tianqi.2345.com/t/wea_history/js/"+months[i]+"/54511_"+months[i]+".js"
    )
print(todo_urls)
import requests
import json
import demjson
import csv
datas = []
for url in todo_urls:
    r = requests.get(url)
    if r.status_code!=200:
        raise Exception()
    # 去除javascript前后的字符串，得到一个js格式的JSON
    data = r.text.lstrip("var weather_str=").rstrip(";")
    datas.append(data)
all_datas=[]
for data in datas:
    tqInfos=demjson.decode(data)["tqInfo"]
    all_datas.extend([x for x in tqInfos if len(x)>0])
with open('C:/Users/Apple/Desktop/beijing_tianqi_2020.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    
    columns = ['ymd', 'bWendu', 'yWendu', 'tianqi', 'fengxiang', 'fengli', 'aqi', 'aqiInfo', 'aqiLevel']
    writer.writerow(columns)
    
    for data in all_datas:
        writer.writerow([data[column] for column in columns])

