import numpy as np
import re
import math

def BusData():
    """
    读取节点数据

    """
    filename = 'IEEE30BusSystemCDF.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    keyStart = 'BUS DATA FOLLOWS                    '
    keyEnd = ' ITEMS\n'
    pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
    result_busnumber = pat.findall(lines[1])
    busnumber = int(result_busnumber[0].strip())
    a = np.zeros((busnumber, 12))
    for i in range(2, busnumber + 2):
        s = list(lines[i])
        # 节点号
        x = ''.join(s[0:4])
        c = int(x.strip())
        a[i - 2][0] = c
        # 节点类型
        x = ''.join(s[24:26])
        c = int(x.strip())
        a[i - 2][1] = c
        # Final voltage
        x = ''.join(s[27:33])
        c = float(x.strip())
        a[i - 2][2] = c
        # final degree
        x = ''.join(s[33:40])
        c = float(x.strip())
        a[i - 2][3] = c
        # Load MW
        x = ''.join(s[40:49])
        c = float(x.strip())
        a[i - 2][4] = c
        # load MVAR
        x = ''.join(s[49:59])
        c = float(x.strip())
        a[i - 2][5] = c
        # generation MW
        x = ''.join(s[59:67])
        c = float(x.strip())
        a[i - 2][6] = c
        # generation MVAR
        x = ''.join(s[67:75])
        c = float(x.strip())
        a[i - 2][7] = c
        # 期望电压KV
        x = ''.join(s[84:90])
        c = float(x.strip())
        a[i - 2][8] = c
        # 节点对地电纳
        x = ''.join(s[114:122])
        c = float(x.strip())
        a[i - 2][9] = c
        # 节点无功的最大值
        x = ''.join(s[90:98])
        c = float(x.strip())
        a[i - 2][10] = c
        # 节点无功的最小值
        x = ''.join(s[98:106])
        c = float(x.strip())
        a[i - 2][11] = c
    return busnumber,a

def BranchData(busnumber):
    filename='IEEE30BusSystemCDF.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    keyStart = 'BRANCH DATA FOLLOWS'
    keyEnd = 'ITEMS\n'
    pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
    result_branchnumber = pat.findall(lines[3+busnumber])
    branchnumber = int(result_branchnumber[0].strip())
    a = np.zeros((branchnumber, 6))  # 用以存储最后的支路数据的数组形式
    b=0
    for k in range(4+busnumber,4+busnumber+branchnumber):
        # 提取节点1
        s = list(lines[k])  # 将result_string列表中的每一个字符串元素拆分成以一个一个字符为元素的列表s
        x = ''.join(s[0:4])
        c = int(x.strip())
        a[b][0] = c
        # 提取节点2
        x = ''.join(s[5:9])
        c = int(x.strip())
        a[b][1] = c
        # 提取支路电阻
        x = ''.join(s[19:29])
        c = float(x.strip())
        a[b][2] = c
        # 提取节点电抗
        x = ''.join(s[29:39])
        c = float(x.strip())
        a[b][3] = c
        # 提取节点电纳
        x = ''.join(s[40:49])
        c = float(x.strip())
        a[b][4] = c
        # 提取线路变压器变比
        x = ''.join(s[76:82])
        c = float(x.strip())
        a[b][5] = c
        b=b+1
    return branchnumber,a

# busname,a=BusData()
# branchname,b=BranchData(busname)
# print(type(a))