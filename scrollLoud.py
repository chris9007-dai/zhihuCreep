import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
def  scroll(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-blink-features=AutomationControlled")#去除selenium的痕迹，防止被反爬虫
    driver = webdriver.Chrome("./chromedriver",chrome_options=options)
    
    cookies = {
        'name':"z_c0",
        'value':'2|1:0|10:1632735897|4:z_c0|92:Mi4xT1VVb0NnQUFBQUFBMEZ6YVdzRzlFeVlBQUFCZ0FsVk5tZUEtWWdDNXhkS1JmXzdGU2ZMcmd6bzZpYi14TldYOVdB|dbd35f4c8c2d1019038bff6083731d8e210ed230ae63a3aaef82befad9e4aaa2',
    }
    driver.get(url)
    driver.add_cookie(cookie_dict=cookies)
    driver.get(url)

        # 创建一个列表，用于记录每一次拖动滚动条后页面的最大高度
    All_Window_Height = []
    # 当前页面的最大高度加入列表
    All_Window_Height.append(driver.execute_script("return document.body.scrollHeight;"))
    while True:
        # 执行拖动滚动条操作
        driver.execute_script("scroll(0,100000)")
        time.sleep(3)
        #获得窗口一半的高度
        halfheight = int(All_Window_Height[-1])/2
        driver.execute_script("scroll(0,{0})".format(halfheight))
        time.sleep(3)
        driver.execute_script("scroll(0,100000)")
        time.sleep(3)
        check_height = driver.execute_script("return document.body.scrollHeight;")
        # 判断拖动滚动条后的最大高度与上一次的最大高度的大小，相等表明到了最底部
        if check_height == All_Window_Height[-1]:
            break
        else:
            # 如果不想等，将当前页面最大高度加入列表。
            All_Window_Height.append(check_height)

    

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    element = soup.find_all("meta",itemprop="url")
    link = re.findall(r"//(.+?)\"",str(element))
    return link




