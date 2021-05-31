import networkx as nx
import matplotlib.pyplot as plt
import readIEEEfile as read
import pandas as pd
import numpy as np

def net_plot():
    busnum, Bus = read.BusData()
    branchnum, Branch = read.BranchData(busnum)
    Busnum=Bus[:,0]
    G=nx.Graph()
    for i in range(0,busnum):
        G.add_node(int(Busnum[i]))
    for i in range(0,branchnum):
        G.add_edge(int(Branch[i][0]),int(Branch[i][1]))
    nx.draw(G)
    plt.savefig('fig.png', bbox_inches='tight')
    plt.show()
    print(G.nodes())

def net_plot1():
    busnum, Bus = read.BusData()
    branchnum, Branch = read.BranchData(busnum)
    net = pd.DataFrame()
    num1=[]
    num2=[]
    for i in range(0,branchnum):
        num1.append(int(Branch[i][0]))
        num2.append(int(Branch[i][1]))
    net['num1']=num1
    net['num2']=num2
    G = nx.from_pandas_edgelist(net, source='num1', target='num2')
    nx.draw(G, with_labels=True, pos=None, arrows=True)
    # plt.savefig("undirected_graph.png")
    plt.show()

def polt2():
    edges = pd.DataFrame()
    edges['sources'] = [0, 1, 2, 3, 4, 4, 6, 7, 7, 9, 1, 4, 4, 4, 6, 7, 5, 8, 9, 8]
    edges['targets'] = [1, 4, 4, 4, 6, 7, 5, 8, 9, 8, 0, 1, 2, 3, 4, 4, 6, 7, 7, 9]
    # edges['weights'] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    G = nx.from_pandas_edgelist(edges, source='sources', target='targets')
    nx.draw(G, with_labels=True, pos=None, arrows=True)
    # plt.savefig("undirected_graph.png")
    plt.show()

def netplot(num1,num2):
    net = pd.DataFrame()
    net['num1']=num1
    net['num2']=num2
    G = nx.from_pandas_edgelist(net, source='num1', target='num2')
    nx.draw(G, with_labels=True, pos=None, arrows=True)
    # plt.savefig("undirected_graph.png")
    plt.show()

def input():
    print("该检索程序是根据输入节点")
    num=input("请输入节点号")
    return num

def find_net(inputnum):
    busnum, Bus = read.BusData()
    # 将所有节点根据电压等级进行分类
    # 计算电压等级的个数与电压等级
    vol_level=[]
    c=1;vol_level.append(Bus[0][12])
    for i in range(1,busnum): # 电压等级的列表
        if Bus[i][12] != Bus[i-1][12]:
            c+=1
            vol_level.append(Bus[i][12])
    volbase={} #电压等级的字典
    Busvol=Bus[:,12];Busvol=np.array(Busvol) #节点数据中基准电压的数组
    # 将每个电压等级下的节点号以字典的形式存储
    for i in range(0,c):
        (b,) = np.array(Busvol == vol_level[i])
        for j in range(0,len(b)):
            b[j] +=1
        volbase.update({vol_level[i]:b})

    #对输入的节点号进行处理
    #找出输入节点所属的电压等级
    for i in range(0,c):
        if inputnum in volbase[vol_level[i]]:
            num_level=vol_level[i]
    plotvol=[] #创建储存画图的电压等级的列表
    for i in range(0,c):  
        if num_level > vol_level[i]:
            plotvol.append(vol_level[i])
    

#net_plot()
net_plot1()

