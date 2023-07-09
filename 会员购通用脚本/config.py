"""
ticket_id填写：购票页面的id
    https://show.bilibili.com/platform/detail.html?id=73710&from=pc_ticketlist
    取 id = 73710

day填写：日期序列号
例如：日期存在
    2023-07-14 周五
    2023-07-15 周六
    2023-07-16 周日
    如果购买【2023-07-15 周六】，则 day = 2

ticket_money：价格序列号
例如：价格存在
    ¥70(预售票)
    ¥120(预售票)
    如果购买【¥70(预售票)】，则 ticket_money = 1

user_list:购票人序列号
例如购买2张票，但绑定了3人信息：
    从左到右依次为：【张三、李四、王五】
    如果张三、王五购票，则user_list=[1, 3]
序列号由左到右，由1开始计数
"""
ticket_id = 73710
day = 2
ticket_money = 1
user_list = [1, 2, 3]

if __name__ == '__main__':
    print("请修改该文件参数")
