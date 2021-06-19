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
    # print(lines[46126])
    # print(lines[337])
    # c=lines[46126].encode('utf-8')
    # cc = lines[337].encode('utf-8')
    # # byte=bytearray(c)
    # byte=c
    # bytecc=cc
    # print('字节数组c')
    # print(byte)
    # print('字节数组d')
    # print(bytecc)
    # byte1=byte[14:18]
    # byte2=bytecc[14:18]
    # print(byte1)
    # print(byte2)
    # # d=c.decode('utf-8')
    # # print(c)
    # # print(d)
    # a=lines[337].encode('gbk')
    # byted=a[14:18]
    # print(byted)
    # print(byted.decode('gbk'))
    # print(a)
    for i in range(0,len(lines)):
        a=lines[i].encode('utf-8')
        #这里需要非常注意的是：因为这个[0:2]本意是想获取每一行中头两个字符，并且该行字符已经暂时被编码为utf-8的格式，
        #如果这两个字节没有中文，那么一个字节就可以代表一个中文，如果含有中文，那么这句代码就只截取了这个中文的utf-8编码
        #的其中一个或两个字节，那么这样是不完整的，在decode中程序是无法解码这个字节，因此会报错
        b=a[0:2]
        check=a[0:1]
        # print(b)
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
    # for num in Ldata:
    #     print(num)
    # print(len(Ldata))
    # print(len(Tdata))
    V500=[]
    print('show 500KV')
    for i in range(0,len(Ldata)):
        #有一些字符gbk是认不出来的，如果报错设置为忽略
        x = Ldata[i].encode('gbk',errors='ignore')
        vdegree = x[14:18]
        y = vdegree.decode('gbk')
        print(y)
        print(i)
        print(Ldata[i])
        # print(type(y))
        if float(y) >= 500:
            V500.append(Ldata[i])



readBPA()