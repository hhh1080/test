import PQpowerflow as PQ
import numpy as np
import EQU
import math

# 形成节点导纳矩阵Y
# Y：节点导纳矩阵 Bus:节点信息 busnum：节点数

Y,Bus,busnum=PQ.YData()

# 进行PQ法潮流计算
# v：电压幅值 o：电压相角

v,o=PQ.PQflow(Y,Bus,busnum)
print(v)
print(o)
allbus=Bus[:,0]
allbus=np.array(allbus)
# allbus=allbus.reshape(busnum,1)
# savebus=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,27,28])
# throwbus,bordenbus,innerbus,YBBnew,YBI,YIB,YII,IBnew,II=EQU.Ward(savebus,allbus,Y,v,o)
# Ynew,Inew=EQU.rebuildWard(YBBnew,YBI,YIB,YII,IBnew,II)
# U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
# EQU.check(Ynew,Inew,bordenbus,innerbus,U)

throwbus=np.array([15,23,24,26],dtype=int)
o=o*math.pi/180
Ynew,Busnew=EQU.CSR(Y,throwbus,allbus,v,o,Bus)
busnumnew=Ynew.shape[0]
v1,o1=PQ.PQflow(Ynew,Busnew,busnumnew)
one=np.ones((len(throwbus)),dtype=int)
# vv1=throwbus-one
# for i in range(0,len(throwbus)):
#     vv1[i]=int(vv1[i])
v=np.delete(v,throwbus - one,axis=0)
deltav=v-v1
print(deltav)
print(len(v1))
print(len(v))
# vv1=deltav.flatten()
print(np.min(deltav))

# savebus=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,27,28])
# o=o*math.pi/180
# throwbus,bordenbus,innerbus,Busnew,Ynew=EQU.Ward1(savebus,allbus,Y,v,o,Bus)
# busnumnew=Ynew.shape[0]
# v2,o2=PQ.PQflow(Ynew,Busnew,busnumnew)
# onebor = np.ones((len(bordenbus)), dtype=int)
# oneinn = np.ones((len(innerbus)), dtype=int)
# U11=v[bordenbus-onebor]
# U22=v[innerbus-oneinn]
# v22=np.concatenate((U11,U22),axis=0)
# print(v22-v2)


# group=np.array([[11,13]])
# group1=np.array([[10,12]])
# o=o*math.pi/180
# Busnew,Ynew=EQU.GenGroup1(group,Bus,v,o,Y)
# busnumnew=Ynew.shape[0]
# v3,o3=PQ.PQflow(Ynew,Busnew,busnumnew)
# U1=np.delete(v,group[0,:],axis=0)
# groupnew=[]
# for i in range(0,group.shape[0]):
#     groupnew.append(int(len(v3)-1+i))
# v4=np.delete(v3,groupnew,axis=0)
# print(U1-v4)