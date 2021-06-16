import re
import numpy as np

def readPFL():
    # PFL文件要先转成TXT文件格式
    filename = 'IEEE39.txt'
    with open(filename,encoding='utf-8') as file_object:
        lines = file_object.readlines()
    d=0
    key = ['control data', 'bus data', 'transmission line data', \
           'end of transformer data', 'UTLC transformer data', \
           'generator data', 'load data']
    linenum=[]
    for i in range(0,len(lines)):
        if key[d] in lines[i]:
            linenum.append(int(i))
            d+=1
        if d == 6:
            break
    # 提取Bus数据创建字典,并存入节点电压幅值和相角
    Bus={}
    busbase=np.zeros((12))
    for a in range(linenum[0]+2,linenum[1]):
        busdata = lines[a].split(" ")
        res = [i.strip() for i in busdata if str(i).strip() != ""]
        busbase[0]=float(res[4]);busbase[1]=float(res[5])
        Bus.update({res[0]:busbase})
    print(Bus['BUS-2'])
    #

readPFL()