import requests
import re
import bs4
import urllib3
import scrollLoud



http = urllib3.PoolManager()
requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5 
session = requests.session()
session.kepp_alive = False

url = "https://www.zhihu.com/topic/19936422/hot"

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Connection':'close'
    
}
""" mainPage = requests.get(url,headers=headers).text
content = bs4.BeautifulSoup(mainPage, "lxml")
element = content.find_all("meta",itemprop="url")

a = re.findall(r"//(.+?)\"",str(element))#提取爬虫网页的文章，问答页面链接 """
a = scrollLoud.scroll(url)
print(len(a))
b = []
for index in range(len(a)):#补全链接
    b.append("https://"+a[index])

for index in b:
    comfirm = re.search(r"zhuanlan",index)
    if(comfirm):
        children = requests.get(index,headers=headers,verify=False).text#请求文章内容
        title = bs4.BeautifulSoup(children,"lxml").find('title') #获取标题
        title = re.findall(r">(.+?)</title>",str(title))[0]
        artical = bs4.BeautifulSoup(children, "lxml").find("div",class_="RichText")#获取内容
        artical = re.findall(r"<p>(.+?)<\/p>",str(artical))
        for a in range(len(artical)):
            with open(title+".txt","a") as f:
                f.write(artical[a]+"\n")
    else:
        children = requests.get(index,headers=headers,verify=False).text#请求问答内容
        title = bs4.BeautifulSoup(children,"lxml").find('title') #获取标题
        title = re.findall(r">(.+?)</title>",str(title))[0]
        artical = bs4.BeautifulSoup(children, "lxml").find("span",class_="RichText")#获取内容
        artical = re.findall(r"<p>(.+?)<\/p>",str(artical))
        for a in range(len(artical)):
            with open(title+".txt","a") as f:
                f.write(artical[a]+"\n")
