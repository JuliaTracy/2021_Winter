import xlrd
import xlwt
limit = 24
readbook = "C:\\Users\\Apple\\Desktop\\kk.xlsx" #原始文件路径
savebook = "C:\\Users\\Apple\\Desktop\\excel" #要保存的目录
data = xlrd.open_workbook(readbook)
# 获取sheet
table = data.sheets()[0]#获取第一个sheet的所有数据
# 行数
nrows = table.nrows
# 列数
ncols = table.ncols
sheets = nrows / limit#总共需要多少excel
for i in range(0, int(sheets)):
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(sheetname="0")#设置sheet名称
    for row in range(1, limit+1):#每次循环limit行
        newRow = row+limit*i
        if newRow < nrows:
            row_content = table.row_values(newRow)
            for col in range(0, ncols):
                worksheet.write(row, col, row_content[col])
    workbook.save(savebook+"\\"+str(i)+".xls")
