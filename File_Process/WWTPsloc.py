# coding=utf-8
import xlrd
import xlwt
def read_xlrd(excelFile):
    data=xlrd.open_workbook(excelFile)
    table=data.sheet_by_index(1)
    i=[]
    pro=[]
    nam=[]
    ene=[]
    for rowNum in range(table.nrows):
        rowVale=table.row_values(rowNum)
        for colNum in range(table.ncols):
            if colNum==0:
                i.append(rowVale[0])
            elif colNum==1:
                pro.append(rowVale[1])
            elif colNum==2:
                nam.append(rowVale[2])
            elif colNum==3:
                ene.append(float(rowVale[3]))
    return i,pro,nam,ene
def read_xlrd1(excelFile):
    data=xlrd.open_workbook(excelFile)
    table=data.sheet_by_index(1)
    i=[]
    pro=[]
    nam=[]
    sca=[]
    lon=[]
    lat=[]
    for rowNum in range(table.nrows):
        rowVale=table.row_values(rowNum)
        for colNum in range(table.ncols):
            if colNum==0:
                i.append(rowVale[0])
            elif colNum==1:
                pro.append(rowVale[1])
            elif colNum==2:
                nam.append(rowVale[2])
            elif colNum==3:
                sca.append(float(rowVale[3]))
            elif colNum==4:
                lon.append(float(rowVale[4]))
            elif colNum==5:
                lat.append(float(rowVale[5]))
    return i,pro,nam,sca,lon,lat
def write_xlwt(value):
    data=xlwt.Workbook(encoding='utf-8')
    table=data.add_sheet('Sheet1')
    for i in range(0,len(value)):
        for j in range(0,7):
            table.write(i,j,value[i][j])
    data.save('C:/Users/Apple/Desktop/1.4/挑战杯/数据/污水处理厂位置规模和能耗.xls')
if __name__=='__main__':
    excelFile1='C:\\Users\\Apple\\Desktop\\1.4\\挑战杯\\数据\\污水处理厂吨水电耗及技术信息\\各年能耗数据\\2019.xlsx'
    excelFile2='C:\\Users\\Apple\\Desktop\\1.4\\挑战杯\\数据\\3.【1,2合并】全国污水处理厂经纬度及建设时间.xlsx'
    i1,pro1,nam1,ene=read_xlrd(excelFile1)
    i2,pro2,nam2,sca,lon,lat=read_xlrd1(excelFile2)
    value=[[0]*7]*len(i2)
    m=0
    for j in range(0,len(i1)):
        for k in range(0,len(i2)):
            if nam1[j] == nam2[k]:
                value[m]=[i1[j],pro1[j],nam1[j],lon[k],lat[k],sca[k],ene[j]]
                m=m+1
                continue
            else:
                pass
    write_xlwt(value)
