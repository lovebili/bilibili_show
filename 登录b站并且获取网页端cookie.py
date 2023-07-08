"""
bilibili网站登录后获取网页端cookie
"""
import time
import json
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 使用的是Chrome浏览器进行登录
web = webdriver.Chrome()
# 填写bilibili的官网链接
web.get('https://www.bilibili.com')
# 先删除以前保存的cookies
web.delete_all_cookies()
# 这个时间用于手动登录,扫码登录可以适当缩短这个等待时间，默认时间为50秒
time.sleep(50)
# 读取登录之后浏览器的cookies
dictcookies = web.get_cookies()
dic={}
dic['bilibili_cookies']=[dictcookies]
# 将字典数据转成json数据便于保存
jsoncookies = json.dumps(dic)
# 写进文本保存
with open('cookie.json','w') as f:
    f.write(jsoncookies)
print('cookies is ok')

web.get('https://www.bilibili.com/bangumi/play/ep316326/?share_source=copy_web&t=10921')

sleep(131003)
