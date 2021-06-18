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
    print(lines[46126])
    c=lines[46126].encode('utf-8')
    d=c.decode('utf-8')
    print(c)
    print(d)
    for i in range(0,len(lines)):
        a=lines[i].encode('utf-8')
        b=a.decode('utf-8')
        if b[0:2] == key1 :
            Lnum.append(int(i))
            Ldata.append(lines[i])
        elif b[0:2] == key2:
            Lnum.append(int(i))
            Tdata.append(lines[i])
    # for num in Lnum:
    #     print(num)
    # print(len(Ldata))
    # print(len(Tdata))
    V500=[]
    for i in range(0,len(Ldata)):
        a = Ldata[i].encode('utf-8')
        b = a.decode('utf-8')
        # print(b[14:18])
    #     vdegree = float(b[14:18])
    #     if vdegree >= 500:
    #         V500.append(Ldata[i])
    # print(len(V500))

readBPA()