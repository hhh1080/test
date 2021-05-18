import numpy as np
import re
import math

np.set_printoptions(suppress=True)


#正则表达式读取节点数
def split_busnumber(file_address):
    """
    使用正则表达式读取ieee格式的文本文件中的节点数
    :param file_address: ieee格式的文本文件的地址
    :return: ieee格式的文本文件中电力系统的节点数
    """
    f = open(file_address)
    keyStart = 'BUS DATA FOLLOWS                    '
    keyEnd = ' ITEMS\n'
    buff = f.read()
    pat = re.compile(keyStart+'(.*?)'+keyEnd, re.S)
    result_busnumber = pat.findall(buff)    #正则表达式，根据有效数据前后的固定信息与格式读出其中的有效数据
    f.close()
    return result_busnumber[0]


#正则表达式读取支路数
def split_branchnumber(file_address):
    """
    使用正则表达式读取ieee格式的文本文件中的支路数
    :param file_address: ieee格式的文本文件的地址
    :return:ieee格式的文本文件中电力系统的支路数
    """
    f = open(file_address)
    keyStart = 'BRANCH DATA FOLLOWS                    '
    keyEnd = ' ITEMS\n'
    buff = f.read()
    pat = re.compile(keyStart+'(.*?)'+keyEnd, re.S)
    result_branchnumber = pat.findall(buff)    #正则表达式，根据有效数据前后的固定信息与格式读出其中的有效数据
    f.close()
    return result_branchnumber[0]


#正则表达式读取节点数据
def split_bus(file_address, n):
    """
    读取文本文件中节点数据的有效信息
    :param file_address:ieee格式的文本文件的地址
    :param n:节点数
    :return:节点数据有效信息的列表形式
    """
    f = open(file_address)
    keyStart = 'BUS DATA FOLLOWS                    '+ n +' ITEMS\n '
    keyEnd = '\n-999'
    buff = f.read()
    pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
    result_list = pat.findall(buff)    #正则表达式，根据有效数据前后的固定信息与格式读出其中的有效数据
    f.close()
    return result_list


#正则表达式读取支路数据
def split_branch(file_address, n):
    """
    读取文本文件中支路数据的有效信息
    :param file_address: ieee格式的文本文件的地址
    :param n: 支路数
    :return: 支路数据有效信息的列表形式
    """
    f = open(file_address)
    keyStart = 'BRANCH DATA FOLLOWS                    '+ n +' ITEMS\n '
    keyEnd = '\n-999'
    buff = f.read()
    pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
    result_list = pat.findall(buff)    #正则表达式，根据有效数据前后的固定信息与格式读出其中的有效数据
    f.close()
    return result_list


#将节点数据列表转化成数组
def turn_bus_matrix(result_bus_list):
    """
    将节点数据的列表形式转成数组形式
    :param result_bus_list: 节点数据有效信息的列表形式
    :return: 节点数据有效信息的数组形式
    """
    result_string = result_bus_list[0].split("\n") #将节点数据列表拆分成以每一行数据为一个字符串的列表
    line=len(result_string)
    a=np.zeros((line,12)) #用以存储最后的节点数据的数组形式
    for k in range(0, line):
        # 节点号
        s = list(result_string[k]) #将result_string列表中的每一个字符串元素拆分成以一个一个字符为元素的列表s
        if k==0:
            s.insert(0,' ')
        x=s[0]+s[1]+s[2]+s[3]
        x = x.strip()
        c = int(x)
        a[k][0] = c
        # 节点类型

        x=s[24]+s[25]
        x = x.strip()
        c = int(x)
        a[k][1] = c
        # Final voltage

        x=s[27]+s[28]+s[29]+s[30]+s[31]+s[32]
        x = x.strip()
        c = float(x)
        a[k][2] = c
        # final degree
        x=s[33]+s[34]+s[35]+s[36]+s[37]+s[38]+s[39]
        x = x.strip()
        c = float(x)
        a[k][3] = c
        # Load MW
        x=s[40]+s[41]+s[42]+s[43]+s[44]+s[45]+s[46]+s[47]+s[48]
        x = x.strip()
        c = float(x)
        a[k][4] = c
        # load MVAR
        x=s[49]+s[50]+s[51]+s[52]+s[53]+s[54]+s[55]+s[56]+s[57]+s[58]
        x = x.strip()
        c = float(x)
        a[k][5] = c
        # generation MW
        x=s[59]+s[60]+s[61]+s[62]+s[63]+s[64]+s[65]+s[66]
        x = x.strip()
        c = float(x)
        a[k][6] = c
        # generation MVAR
        x=s[67]+s[68]+s[69]+s[70]+s[71]+s[72]+s[73]+s[74]
        x = x.strip()
        c = float(x)
        a[k][7] = c
       # 期望电压KV
        x=s[84]+s[85]+s[86]+s[87]+s[88]+s[89]
        x = x.strip()
        c = float(x)
        a[k][8] = c
        # 节点对地电纳
        x=s[114]+s[115]+s[116]+s[117]+s[118]+s[119]+s[120]+s[121]
        x = x.strip()
        c = float(x)
        a[k][9] = c
        # 节点无功的最大值
        x=s[90]+s[91]+s[92]+s[93]+s[94]+s[95]+s[96]+s[97]
        x = x.strip()
        c = float(x)
        a[k][10] = c
        # 节点无功的最小值
        x=s[98]+s[99]+s[100]+s[101]+s[102]+s[103]+s[104]+s[105]
        x = x.strip()
        c = float(x)
        a[k][11] = c
    node_branch_mat = a
    return node_branch_mat


#将支路数据从列表转换成数组
def turn_branch_array(result_branch_list):
    """
    将支路数据的列表形式转成数组形式
    :param result_branch_list: 支路数据有效信息的列表形式
    :return: 支路数据有效信息的数组形式
    """
    result_string = result_branch_list[0].split("\n")#将支路数据列表拆分成以每一行数据为一个字符串的列表
    line=len(result_string)
    a=np.zeros((line,6))#用以存储最后的支路数据的数组形式
    for k in range(0, line):
        # 提取节点1
        s = list(result_string[k])#将result_string列表中的每一个字符串元素拆分成以一个一个字符为元素的列表s
        if k==0:
            s.insert(0,' ')
        x=s[0]+s[1]+s[2]+s[3]
        x = x.strip()
        c = int(x)
        a[k][0] = c
        # 提取节点2
        x=s[5]+s[6]+s[7]+s[8]
        x = x.strip()
        c = int(x)
        a[k][1] = c
        # 提取支路电阻
        x=s[19]+s[20]+s[21]+s[22]+s[23]+s[24]+s[25]+s[26]+s[27]+s[28]
        x = x.strip()
        c = float(x)
        a[k][2] = c
        # 提取节点电抗
        x=s[29]+s[30]+s[31]+s[32]+s[33]+s[34]+s[35]+s[36]+s[37]+s[38]
        x = x.strip()
        c = float(x)
        a[k][3] = c
        # 提取节点电纳
        x=s[40]+s[41]+s[42]+s[43]+s[44]+s[45]+s[46]+s[47]+s[48]
        x = x.strip()
        c = float(x)
        a[k][4] = c
        # 提取节点电导
        x=s[76]+s[77]+s[78]+s[79]+s[80]+s[81]
        x = x.strip()
        c = float(x)
        a[k][5] = c
    node_branch_array = a
    return node_branch_array