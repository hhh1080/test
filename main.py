import PQpowerflow as PQ
import numpy as np
import EQU

Y,Bus,busnum=PQ.YData()
v,o=PQ.PQflow(Y,Bus,busnum)
print(v)
print(o)
allbus=Bus[:,0]
allbus=np.array(allbus)
# allbus=allbus.reshape(busnum,1)
savebus=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,27,28])
throwbus,bordenbus,innerbus,YBBnew,YBI,YIB,YII,IBnew,II=EQU.Ward(savebus,allbus,Y,v,o)
Ynew,Inew=EQU.rebuildWard(YBBnew,YBI,YIB,YII,IBnew,II)
U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
EQU.check(Ynew,Inew,bordenbus,innerbus,U)
