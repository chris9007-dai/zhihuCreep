<h1 align="center">知乎文章，回答爬虫<h1>

**1、依赖：** 

​		1、bs4 

​		2、urllib3

​		3、scrollLoud

​		4、jieba

​		5、selenium

**2、articalScreeper.py**

​		该脚本会爬取知乎链接内的文章，回答的链接，再解析链接中的文本，存为txt文本

​		修改脚本中下方代码的地址

```
url = "https://www.zhihu.com/topic/19936422/hot"
```

**3、scrollLoud.py**

​		1、因页面有懒加载，为抓取整个页面内容，需要滚动 滚动条

​				所以用到chromedriver(自动化测试的浏览器版本，项目中有)和selenium(模块)

​		2、知乎需要登陆后才能访问，需要登陆cookie，填入下方代码的name，value中

```
cookies = {
        'name':"z_c0",
        'value':'2|1:0|10:1632735897|4:z_c0|92:Mi4xT1VVb0NnQUFBQUFBMEZ6YVdzRzlFeVlBQUFCZ0FsVk5tZUEtWWdDNXhkS1JmXzdGU2ZMcmd6bzZpYi14TldYOVdB|dbd35f4c8c2d1019038bff6083731d8e210ed230ae63a3aaef82befad9e4aaa2',
    }
```

**3、jie.py**

​		1、分词库，会读取本目录中的所有txt文本，分析出出现次数最多的词汇按多到小排序，存为txt文档

​		2、修改下方代码（）中的值，可以设置词汇的数量

```
for i in range(100):
```

**4、delete.py**

​		删除本目录中的所有txt文件