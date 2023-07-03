import requests
import io
import sys
import json
import csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 请在改变下面的文件名
f = open('bilibili会员购漫展演出查询.csv','a',encoding='utf-8')

csv_writer = csv.writer(f)
csv_writer.writerow(["会员购漫展演出对应的id","演出名称","演出时间","演出地点"])
csv_writer = csv.writer(f)
a=int(input('请输入爬取开始值，如：15000\n'))
b=int(input('请输入爬取结束值，如：25000\n'))
manzahnid=0
for manzahnid in range(a,b):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.0 Safari/537.36'
        }
    # 漫展演出的信息api如下
    url='https://show.bilibili.com/api/ticket/project/get?version=134&id='+str(manzahnid)


# 数据处理与储存
# 接下来就是依托屎山代码且会有报错，因为作者是个纱币而且懒得更改



    # 获取源信息
    soure1=requests.get(url=url,headers=headers1)
    soure1_2=soure1.text
    # 设置一个环节用于检测是否有内容
    soure1_3 = json.loads(soure1_2)
    print(soure1_3 )
    # 设置一个环节用于检测是否有内容
    data3   =soure1_3.get('msg')
    print(data3)
    if data3 == '':

        data1   =soure1_3.get("data",'none')
        data1_1=data1.get("screen_list",'none')
        name1  =data1.get("name")

        # 演出的会员购id
        print("演出的会员购id",manzahnid)
        # 演出名称
        yanchu_name=name1
        print("演出的名称",name1)



        data1_2 = data1.get("performance_desc", 'none')
        # 判断类型
        pand_uan=data1_2.get("type", 'none')
        if pand_uan==1:

            try:
                data1_2_2 = data1_2.get("list", 'none')
                data1_2_2_2 = data1_2_2[2]
                data1_2_2_2_2 = data1_2_2_2.get("details", 'none')
                # 演出的时间
                data1_2_2_2_2_2 = data1_2_2_2_2[0]
                data1_2_2_2_2_2_2 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_time = data1_2_2_2_2_2_2
                print("演出的时间", data1_2_2_2_2_2_2)
                # 演出的地点
                00
                data1_2_2_2_2_2 = data1_2_2_2_2[1]
                data1_2_2_2_2_2_3 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_addres = data1_2_2_2_2_2_3
                print("演出的地点", data1_2_2_2_2_2_3)
                csv_writer.writerow([manzahnid,yanchu_name,yanchu_time, yanchu_addres])
            except:
                data1_2_2 = data1_2.get("list", 'none')
                data1_2_2_2 = data1_2_2[1]
                data1_2_2_2_2 = data1_2_2_2.get("details", 'none')
                # 演出的时间
                data1_2_2_2_2_2 = data1_2_2_2_2[0]
                data1_2_2_2_2_2_2 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_time = data1_2_2_2_2_2_2
                print("演出的时间", data1_2_2_2_2_2_2)
                # 演出的地点
                data1_2_2_2_2_2 = data1_2_2_2_2[1]
                data1_2_2_2_2_2_3 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_addres = data1_2_2_2_2_2_3
                print("演出的地点", data1_2_2_2_2_2_3)
                csv_writer.writerow([manzahnid, yanchu_name, yanchu_time, yanchu_addres])

        else :
            try:
                data1_2_2 = data1_2.get("list", 'none')
                data1_2_2_2 = data1_2_2[1]
                data1_2_2_2_2 = data1_2_2_2.get("details", 'none')
                # 演出的时间
                data1_2_2_2_2_2 = data1_2_2_2_2[0]
                data1_2_2_2_2_2_2 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_time = data1_2_2_2_2_2_2
                print("演出的时间", data1_2_2_2_2_2_2)
                # 演出的地点
                data1_2_2_2_2_2 = data1_2_2_2_2[1]
                data1_2_2_2_2_2_3 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_addres = data1_2_2_2_2_2_3
                print("演出的地点", data1_2_2_2_2_2_3)
                csv_writer.writerow([manzahnid, yanchu_name, yanchu_time, yanchu_addres])
            except:
                data1_2_2 = data1_2.get("list", 'none')
                data1_2_2_2 = data1_2_2[2]
                data1_2_2_2_2 = data1_2_2_2.get("details", 'none')
                # 演出的时间
                data1_2_2_2_2_2 = data1_2_2_2_2[0]
                data1_2_2_2_2_2_2 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_time = data1_2_2_2_2_2_2
                print("演出的时间", data1_2_2_2_2_2_2)
                # 演出的地点
                data1_2_2_2_2_2 = data1_2_2_2_2[1]
                data1_2_2_2_2_2_3 = data1_2_2_2_2_2.get("content", 'none')
                yanchu_addres = data1_2_2_2_2_2_3
                print("演出的地点", data1_2_2_2_2_2_3)
                csv_writer.writerow([manzahnid, yanchu_name, yanchu_time, yanchu_addres])

    else:
        #漫展演出id后，没有内容或未公布
        yanchu_time=''
        yanchu_addres=''
        yanchu_name = ''
        csv_writer.writerow([manzahnid,yanchu_name,yanchu_time, yanchu_addres])
