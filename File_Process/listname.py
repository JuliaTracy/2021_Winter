# -*- coding: utf-8 -*- 
import os 
import xlwt
name=[]
def listdir(path, list_name):
  filename=[]
  for file in os.listdir(path): 
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path): 
      listdir(file_path, list_name) 
    elif os.path.splitext(file_path)[1]=='.shp': 
      list_name.append(file_path)
listdir(r"C:\Users\Apple\Desktop\1.11\地级市\地级市", name)
def write_excel(path, value):
    workbook=xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)
    for i in range(0,len(value)):
        sheet.write(i,0,value[i])
    workbook.save(path)
write_excel(r"C:\Users\Apple\Desktop\1.11\地级市\file.xls",name)

    
