#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
n=0
path = r"C:\Users\lenovo\Desktop\1.18\虚拟城市\地级市\相交"
for root,dirs,files in os.walk(path):
    for filename in files:
        if filename.startswith('形心点'):
            os.remove(os.path.join(root,filename))
            n+=1       
print('共删除%s个文件'%n)
