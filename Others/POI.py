# -*- coding:utf-8 -*
import json  #导入json库
import os
import urllib2 #导入urllib2库
import sys #把默认编码从ascii转到uft-8
reload(sys)
sys.setdefaultencoding('utf-8')
#可变
lat_1=3.86
lon_1=73.66
lat_2=53.55
lon_2=135.05   #坐标范围
las=1  #给las一个值1
ak='' #我的百度地图ak
keyword='医院'
push=r'C:\Users\Apple\Desktop\hospital.txt'
#
f=open(push,'a')
lat_count=int((lat_2-lat_1)/las+1)
lon_count=int((lon_2-lon_1)/las+1)
for lat_c in range(0,lat_count):
    lat_b1=lat_1+las*lat_c
    for lon_c in range(0,lon_count):
        lon_b1=lon_1+las*lon_c
        for i in range(0,20):
            page_num=str(i)
            url='http://api.map.baidu.com/place/v2/search?query='keyword'& bounds='+str(lat_b1)+','+str(lon_b1)+','+str(lat_b1+las)+','+str(lon_b1+las)+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
            response = urllib2.urlopen(url2)
            data=json.load(response)
            for item in data['results']:
                jname=item['name']
                jlat=item['location']['lat']
                jlon=item['location']['lng']
                jadd=item['address']
                j_str=jname+','+str(jlat)+','+str(jlon)+','+jadd+'\n'
                f.write(j_str)
f.close()















