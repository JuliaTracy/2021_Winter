import csv
def csv_process(filepath):
    with open(filepath,mode='r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
def main():
    filepath = input('请输入文件名称：')
    csv_process(filepath)
if __name__ == '__main__':
    main()
