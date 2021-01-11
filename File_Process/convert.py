import os
cwd = os.getcwd()
read_path = 'excel'
os.chdir(read_path)
files = os.listdir()
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == '.xls':
        newname = portion[0] + '.csv'
        os.rename(filename, newname)
