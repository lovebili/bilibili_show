import datetime
import time
import pyttsx3
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init()
buy_url = "https://show.bilibili.com/platform/detail.html?id=73710&from=pc_ticketlist"

day = int(input("\n请输入购票的日期，1表示21号，2表示22号，3表示23号\n"))
user_lis = input("\n请输入购票人员身份序列号，以空格分隔（例如第1、3、4人则输入：1 3 4）：")
user_list = user_lis.split(" ")
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print("{}:{}".format(day, user_list))

# 设置购票的日期
day_xpath = f"/html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[" + str(day) + "]"
# 该日期为21日票 /html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[1]/li[2]/div[1]

# 在这里设置购票的种类
tick_xpath = f"/html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[2]/li[2]/div[3]"

# /html/body/div/div[2]/div[2]/div[2]/div[2]/div[4]/ul[2]/li[2]/div[4]这个是780元的价格的c区

# 加载配置文件
with open('./cookie.json', 'r') as f:
    config = json.load(f)


def voice(message):
    engine.setProperty('volume', 1.0)
    engine.say(message)
    engine.runAndWait()
    engine.stop()
    voice(message)


# 设置抢购时间
TargetTime = "2013-10-3 8:00:00.00000000"

WebDriver = webdriver.Chrome()
wait = WebDriverWait(WebDriver, 0.5)
if len(config["bilibili_cookies"]) == 0:
    # 输入目标购买页面
    WebDriver.get(buy_url)
    WebDriver.maximize_window()
    time.sleep(1)
    WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
    print("请登录")
    while True:
        try:
            WebDriver.find_element(By.CLASS_NAME, "nav-header-register")
        except:
            break
    time.sleep(5)
    config["bilibili_cookies"] = WebDriver.get_cookies()
    with open('./cookie.json', 'w') as f:
        json.dump(config, f, indent=4)
else:
    WebDriver.get(buy_url)  # 输入目标购买页面
    # 弹窗按钮
    try:
        WebDriver.find_element(By.CLASS_NAME, "real-name-modal-confirm-btn").click()
    except:
        pass
    for cookie in config["bilibili_cookies"]:  # 利用cookies登录账号
        WebDriver.add_cookie(cookie)
        WebDriver.maximize_window()

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now + "     " + TargetTime)
    if now >= TargetTime:
        WebDriver.refresh()
        break

while True:
    try:
        if day_xpath != "":
            element = wait.until(EC.visibility_of_element_located(
                (By.XPATH, day_xpath)))
            element.click()
            # 增加购买人数
            element = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "count-plus")))
            for i in range(len(user_list)):
                element.click()

            # element = wait.until(EC.visibility_of_element_located(
            # (By.XPATH, tick_xpath)))
            # element.click()
        # 等待抢票按钮出现并可点击
        element = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'product-buy.enable')))
        # 点击抢票按钮
        element.click()

        # time.sleep(5)
        print("进入购买页面成功")
        break
    except:
        WebDriver.refresh()
        continue
# 选择购票人
while True:
    try:
        user_str = 'card-item-container'
        element = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, user_str)))

        elements = WebDriver.find_elements(By.CLASS_NAME, "card-item-container")
        # for i in elements:
        #     if not i.find_elements(By.CLASS_NAME, "icon-checked"):
        #         i.click()
        for i in user_list:
            i = int(i) - 1
            elements = WebDriver.find_elements(By.CLASS_NAME, "card-item-container")[i]
            elements.click()
        break
    except:
        WebDriver.refresh()
        continue

element = None
while element is None:
    try:
        # 打勾：我以知晓
        check = WebDriver.find_element(By.CLASS_NAME, "check-icon.checked")
        if not EC.element_to_be_selected(check):
            check.click()
        element = WebDriver.find_element(By.CLASS_NAME, "confirm-paybtn.active")
    except:
        continue
element.click()
print("订单创建完成，请在一分钟内付款")
voice('二次元，你的票买到了，快付款')
# 语音提醒时间
time.sleep(60)
while True:
    try:  # 确认协议按钮iki
        quereng_button = WebDriver.find_elements(By.XPATH,
                                                 "/html/body/div/div[2]/div/div[5]/div[1]/div/span[1]").click()
        # 确认支付按钮
        quereng_zhifu_button = WebDriver.find_elements(By.XPATH, "/html/body/div/div[2]/div/div[5]/div[2]").click()
        print("该付款了")
    except:
        continue
time.sleep(230721)
