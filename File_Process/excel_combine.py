import pandas as pd
import os
import csv
import numpy as np
read_path = r'C:\Users\Apple\Desktop\excel'
save_path = r'C:\Users\Apple\Desktop\excel_merge'
save_name = r'modified.csv'
os.chdir(read_path)
csv_name_list = os.listdir()
df = pd.read_csv(read_path+'\\'+csv_name_list[0], encoding='ISO-8859-1',error_bad_lines=False)
df.to_csv(save_path + '\\' + save_name, encoding="utf_8_sig", index=False)
for i in range(1, 2167):
    df = pd.read_csv(read_path+'\\'+csv_name_list[i],encoding='ISO-8859-1',error_bad_lines=False)
    df1=pd.concat(df,axis=1)
    df1.to_csv(save_path+ '\\' + save_name ,encoding="utf_8_sig",index=False, header=False, mode='a+')
