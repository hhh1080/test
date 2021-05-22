import math
import numpy as np

def Ward(savebus,allbus,Y,v,o):
    allbus1=allbus.tolist()
    savebus1=savebus.tolist()
    throwbus1=list(set(allbus1).difference(set(savebus1)))
    throwbus=np.array(throwbus1)
    bordenbus=[]
    for i in range(0,len(savebus)):
        for j in range(0,len(throwbus)):
            if Y[int(savebus[i]-1),int(throwbus[j]-1)] != 0:
                bordenbus.append(int(savebus[i]))
                break
    # bordenbus=np.array(bordenbus)
    # innerbus1=[]
    innerbus1=list(set(savebus1).difference(set(bordenbus)))
    bordenbus = np.array(bordenbus)
    innerbus=np.array(innerbus1)
    U=v*np.cos(o)+v*np.sin(o)*complex(0,1)
    I=np.matmul(Y,U)
    YII=np.zeros((len(innerbus),len(innerbus)),dtype=complex)
    for i in range(0,len(innerbus)):
        for j in range(0,len(innerbus)):
            YII[i,j]=Y[int(innerbus[i]-1),int(innerbus[j]-1)]
    YIB=np.zeros((len(innerbus),len(bordenbus)),dtype=complex)
    for i in range(0,len(innerbus)):
        for j in range(0,len(bordenbus)):
            YIB[i,j]=Y[int(innerbus[i]-1),int(bordenbus[j]-1)]
    YBI = np.zeros((len(bordenbus), len(innerbus)),dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(innerbus)):
            YBI[i, j] = Y[int(bordenbus[i]-1), int(innerbus[j]-1)]
    YBB = np.zeros((len(bordenbus), len(bordenbus)),dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(bordenbus)):
            YBB[i, j] = Y[int(bordenbus[i]-1), int(bordenbus[j]-1)]
    YBE = np.zeros((len(bordenbus), len(throwbus)),dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(throwbus)):
            YBE[i, j] = Y[int(bordenbus[i]-1), int(throwbus[j]-1)]
    YEB = np.zeros((len(throwbus), len(bordenbus)),dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(bordenbus)):
            YEB[i, j] = Y[int(throwbus[i] - 1), int(bordenbus[j] - 1)]
    YEE = np.zeros((len(throwbus), len(throwbus)),dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(throwbus)):
            YEE[i, j] = Y[int(throwbus[i] - 1), int(throwbus[j] - 1)]
    YBBnew=YBB-np.matmul(np.matmul(YBE,np.linalg.inv(YEE)),YEB)
    IB=np.zeros((len(bordenbus),1),dtype=complex)
    II=np.zeros((len(innerbus),1),dtype=complex)
    for i in range(0,len(bordenbus)):
        IB[i][0]=I[int(bordenbus[i]-1)][0]
    for i in range(0,len(innerbus)):
        II[i][0]=I[int(innerbus[i]-1)][0]
    IE = np.zeros((len(throwbus),1),dtype=complex)
    for i in range(0, len(throwbus)):
        IE[i][0] = I[int(throwbus[i] - 1)][0]
    IBnew=IB-np.matmul(np.matmul(YBE,np.linalg.inv(YEE)),IE)
    return throwbus,bordenbus,innerbus,YBBnew,YBI,YIB,YII,IBnew,II

def rebuildWard(YBBnew,YBI,YIB,YII,IBnew,II):
    Y1=np.concatenate((YBBnew,YBI),axis=1)
    Y2=np.concatenate((YIB,YII),axis=1)
    Ynew=np.concatenate((Y1,Y2),axis=0)
    Inew=np.concatenate((IBnew,II),axis=0)
    return Ynew,Inew

def check(Ynew,Inew,bordenbus,innerbus,U):
    Unew=np.linalg.solve(Ynew,Inew)
    U1=np.zeros((len(bordenbus)+len(innerbus),1),dtype=complex)
    for i in range(0,len(bordenbus)):
        U1[i][0]=U[int(bordenbus[i]-1)][0]
    d=0
    for i in range(len(bordenbus),len(bordenbus)+len(innerbus)):
        U1[i][0]=U[int(innerbus[d]-1)][0]
        d+=1
    deltaU=Unew-U1
    print(deltaU)