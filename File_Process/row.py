import os
import linecache
province=['安徽','北京','福建','甘肃','广东','广西','贵州','海南','河北','河南','黑龙江','湖北','湖南','吉林','江苏','江西','辽宁','内蒙古','宁夏','青海','山东','山西','陕西','上海','四川','天津','西藏','新疆','云南','浙江','重庆']
for i in range(0,31):
    root='C:/Users/Apple/Desktop/11.30/全国降雨/'+province[i]+"/" 
    file_names = os.listdir(root)    
    file_ob_list=[]   
    for file_name in file_names:      
        filedir=root+'\\'+file_name
        file_ob_list.append(filedir)      

    print(file_ob_list)  

    filename='C:/Users/Apple/Desktop/11.30/全国降雨/'+province[i]+"/"+province[i]+'.txt'  
    with open(filename,'w') as f:
        for file in file_ob_list:
            count=-1
            for count,line in enumerate(open(file,'rU').readlines()):
                count+=1
            if (count==-1):
                count+=1
            print(count)
            f.writelines([str(file[-10:-4]),':',' ',str(count),'\r\n'])
        f.close
