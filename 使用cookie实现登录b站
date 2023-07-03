"""
bilibili网页端使用cookie实现登录
"""
import time
import json
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
web = webdriver.Chrome()
web.get('https://www.bilibili.com')

# 读取文件中的cookies数据
f = open('cookie.json','r')
listcookie = json.loads(f.read())
# 将cookies数据添加到浏览器
for cookie in listcookie:
    web.add_cookie(cookie)
# 刷新网页
web.refresh()

print('请查看登录结果')

web.get('https://www.bilibili.com')
web.get('https://www.bilibili.com/bangumi/play/ep316347/?share_source=copy_web&t=6392')

sleep(230723)
