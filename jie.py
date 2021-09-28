import jieba
import os
data = []   #存。txt文件名
for files in os.listdir("./"): #读取当前文件夹。txt文件名
    if os.path.splitext(files)[1] == '.txt':
        data.append(files)
words = []  #存放词汇
for index in data :
    txt = open(index,'r',encoding='utf-8').read()
    words += jieba.lcut(txt) #解析词汇，并存入
counts = {} #存放词汇出现次数
for word in words: 
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1 #遍历所有词汇，每出现一次架+1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True) #根据词语出现的次数从大到小排序
result = {}
for i in range(100):
    word,count = items[i]
    result[word] = count

with open("result.txt","w") as f:
    f.write(str(result))
