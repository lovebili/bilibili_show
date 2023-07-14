import json
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as ex
import config
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
web = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(web, timeout=5, poll_frequency=0.2)

with open("stealth.min.js", "r", encoding="utf8") as f:
    js_str = f.read()
web.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js_str})
"""
获取登录状态：https://api.bilibili.com/x/web-interface/nav/stat
获取订单记录：https://show.bilibili.com/api/ticket/order/list?page=0&page_size=10


详情页：https://show.bilibili.com/platform/detail.html
订单页：https://show.bilibili.com/platform/confirmOrder.html
"""

# user_list = [1, 2]
# buy_day = 2
# buy_ticket = 1

user_list = config.user_list
buy_day = config.day
buy_ticket = config.ticket_money


def login():
    url = 'https://www.bilibili.com'
    web.get(url)
    web.delete_all_cookies()
    # print(web.find_element(By.CLASS_NAME, "header-login-entry"))
    while True:
        time.sleep(3)
        try:
            web.find_element(By.CLASS_NAME, "header-login-entry")
        except:
            bili_cookie = web.get_cookies()
            print(bili_cookie)
            with open("cookie.txt", "w", encoding="utf8") as f:
                f.write(str(bili_cookie))
            break


def set_cookie():
    with open("cookie.txt", "r", encoding="utf8") as f:
        cookie = f.read()
    cookie = eval(cookie)
    url = 'https://www.bilibili.com'
    web.get(url)
    for i in cookie:
        web.add_cookie(cookie_dict=i)
    # web.refresh()
    url = 'https://api.bilibili.com/x/web-interface/nav/stat'
    web.get(url)
    status_text = web.find_element(By.TAG_NAME, "body").text
    status_text = eval(status_text)
    if status_text["code"] == -101:
        print("cookies失效,重新登陆")
        login()


def detail():
    url = "https://show.bilibili.com/platform/detail.html?id={}&from=pc_ticketlist".format(config.ticket_id)
    # url = "https://show.bilibili.com/platform/detail.html?id=73710&from=pc_ticketlist"
    web.get(url)
    # 弹窗按钮
    try:
        web.find_element(By.CLASS_NAME, "real-name-modal-confirm-btn").click()
    except:
        pass
    # 加载出detail
    while True:
        try:
            ele = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "detail-info-wrapper")))
            # print(ele)
            break
        except ex.NoSuchElementException as e:
            # print(e)
            continue

    def detail_select():
        try:
            # 日期
            day = ele.find_element(By.CLASS_NAME, "screens")
            # for i in day.find_elements(By.TAG_NAME, "div"):
            #     print(i.text)
            day.find_elements(By.TAG_NAME, "div")[buy_day - 1].click()
        except ex.ElementClickInterceptedException as e:
            print(e)

        try:
            # 价格
            tick = ele.find_element(By.CLASS_NAME, "tickets")
            # for i in tick.find_elements(By.TAG_NAME, "div"):
            #     print(i.text)
            tick.find_elements(By.TAG_NAME, "div")[buy_ticket - 1].click()
        except ex.ElementClickInterceptedException as e:
            print(e)

        # 数量
        count = ele.find_element(By.CLASS_NAME, "count-plus")
        try:
            for i in range(1, len(user_list)):
                count.click()
        except ex.ElementClickInterceptedException as e:
            print(e)

    while True:
        # 提交按钮
        buy_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-buy')))
        if "立即购票" in buy_button.text:
            detail_select()
            buy_button.click()
            break
        else:
            print("\r{} 当前无票，刷新网页！".format(time.strftime("%H:%M:%S", time.localtime())), end="")
            web.refresh()
            time.sleep(5)
            continue
    print("\n")


def confirm_order():
    # 选人
    while True:
        try:
            # ele=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-item-container")))
            ele = web.find_elements(By.CLASS_NAME, "card-item-container")
            for i in user_list:
                i = int(i) - 1
                elements = ele[i]
                elements.click()
            break
        except IndexError:
            print("购买票数与人数不对应，但继续提交！")
            break
        except ex.NoSuchElementException as e:
            print(e)
            continue
    # 提交订单
    element = None
    while element is None:
        try:
            # 打勾：我以知晓
            check = web.find_element(By.CLASS_NAME, "check-icon.checked")
            if not EC.element_to_be_selected(check):
                check.click()
            element = web.find_element(By.CLASS_NAME, "confirm-paybtn.active")
        except ex.NoSuchElementException:
            continue
    print("is ok")
    element.click()


def retry():  # 热门票抢购会有retry弹窗
    while True:
        if "confirmOrder.html" not in web.current_url:
            return -1
        print("{} retry".format(time.strftime("%H:%M:%S", time.localtime())))
        time.sleep(0.2)
        try:
            ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "retry-btn")))
            if ele:
                ele.click()
                continue
        except ex.TimeoutException:  # 此时不能继续retry，需要点击狗购票按钮
            ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-paybtn.active")))
            try:
                if ele:
                    ele.click()
            except ex.ElementClickInterceptedException:  # 提交按钮不可被点击
                print("完成！")
                break
        except BaseException as e:
            print(e)
            break
    return 0


def captcha():
    # 存在滑块验证码则一直等待
    while True:
        time.sleep(1.5)
        try:
            ele = web.find_element(By.CLASS_NAME, "geetest_canvas_fullbg")
        except(ex.TimeoutException, ex.NoSuchElementException):
            break


# def config_file():
#     config_text = """
#                     ticket_id = 73710
#                     day = 2
#                     ticket_money = 1
#                     user_list = "1 3 4"
#                     cookie = ""
#                 """
#     with open("con.py", "w", encoding="utf8") as f:
#         f.write(config_text)


def menu():
    menu_text = "{:-^40}\n" \
                "{}\n" \
                "{}\n" \
                "{:-^40}".format("menu", "1.登录并获取cookies", "2.存在cookies并开始运行", "")
    print(menu_text)
    num = int(input("输入序号："))
    if num == 1:
        login()
        web.quit()
    if num == 2:
        while True:
            set_cookie()
            detail()
            captcha()
            if "confirmOrder.html" in web.current_url:
                confirm_order()
                if retry() != 0:
                    continue
                break
            else:
                continue
    time.sleep(60)


if __name__ == '__main__':
    menu()
    # config_file()
