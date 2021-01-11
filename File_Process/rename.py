#-*- coding: utf-8 -*-
import os
import re
province=['黑龙江','内蒙古']
def rename():
    for i in range(0,2):
        path="C:/Users/Apple/Desktop/11.30/全国降雨/"+province[i]+"/"
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        for files in filelist:#遍历所有文件
            Olddir=os.path.join(path,files)#原来的文件路径
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                continue
            filename=os.path.splitext(files)[0]#文件名
            '''if (province[i]=='黑龙江') or (province[i]=='内蒙古'):
                name=filename[3:8]
            else:
                name=filename[2:7]'''
            name=re.sub("\D","",filename)
            filetype=os.path.splitext(files)[1]#文件扩展名
            Newdir=os.path.join(path,name+filetype)#新的文件路径
            os.rename(Olddir,Newdir)#重命名
if __name__=='__main__':
    rename()
