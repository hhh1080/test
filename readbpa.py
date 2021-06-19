import re
import numpy as np

def readBPA():
    #将BPA文件转换为utf-8格式的TXT文件
    filename='NF2021DD.txt'
    #将BPA数据文件每一行每一行地读取
    with open(filename,encoding='utf-8') as file_object:
        lines = file_object.readlines()
    Lnum=[]
    Ldata=[]
    Tdata=[]
    key1 = 'L ';key2 = 'T '
    #找到头两个字符为L（即线路卡片）的数据行，方法是将每一行的字符编码为utf-8。再以同样格式解码就可以提取
    #字符串中的任意一个字符
    for i in range(0,len(lines)):
        a=lines[i].encode('utf-8')
        #这里需要非常注意的是：因为这个[0:2]本意是想获取每一行中头两个字符，并且该行字符已经暂时被编码为utf-8的格式，
        #如果这两个字节没有中文，那么一个字节就可以代表一个字符，如果含有中文，那么这句代码就只截取了这个中文的utf-8编码
        #的其中一个或两个字节，那么这样是不完整的，在decode中程序是无法解码这个字节，因此会报错
        b=a[0:2]
        #不读取注释卡
        check=a[0:1]
        checkstr = check.decode('utf-8')
        if checkstr == '.':
            continue
        c=b.decode('utf-8')
        if c == key1 :
            Lnum.append(int(i))
            Ldata.append(lines[i])
        elif c == key2:
            Lnum.append(int(i))
            Tdata.append(lines[i])
    return Ldata,Tdata


def find500bus(Ldata):
    # 找出500KV电压等级的线路
    V500lines = []
    print('show 500KV')
    for i in range(0, len(Ldata)):
        # gbk编码中汉字是用两个字节表示，和BPA数据格式对应
        # 有一些字符gbk是认不出来的，如果报错设置为忽略
        x = Ldata[i].encode('gbk', errors='ignore')
        vdegree = x[14:18]
        y = vdegree.decode('gbk')
        print(y)
        print(i)
        print(Ldata[i])
        if float(y) >= 500:
            V500lines.append(Ldata[i])
    # 找出500KV线路上的节点
    V500bus = []
    for i in range(0, len(V500lines)):
        x = V500lines[i].encode('gbk', errors='ignore')
        busname1 = x[6:14]
        busname2 = x[19:27]
        y1 = busname1.decode('gbk')
        y2 = busname2.decode('gbk')
        if y1 not in V500bus:
            V500bus.append(y1)
        if y2 not in V500bus:
            V500bus.append(y2)
    print(V500bus)
    return V500bus

def findnet():
    while True:
        bus500 = input('请输入500KV节点名称')
        if bus500 in V500bus:
            break


Ldata,Tdata=readBPA()
V500bus=find500bus(Ldata)