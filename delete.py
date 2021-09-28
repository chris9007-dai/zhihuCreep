import os

filePath = []   #存.txt文件名
for files in os.listdir("./"): #读取当前文件夹.txt文件名
    if os.path.splitext(files)[1] == '.txt':
        filePath.append(files)
for file in filePath:#删除.txt文件
    if os.path.exists(file):
        os.remove(str(file))