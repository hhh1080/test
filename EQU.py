import math
import numpy as np

def Ward(savebus,allbus,Y,v,o):
    throwbus=list(set(allbus).difference(set(savebus)))
    bordenbus=[]
    for i in range(0,len(throwbus)):
        for j in range(0,Y.shape[0]):
            if Y[j,throwbus[i]] !=0:
                bordenbus.append(j+1)
    bordenbus=np.array(bordenbus)
    innerbus=list(set(savebus).difference(set(bordenbus)))
    U=v*np.cos(o)+v*np.sin(o)*complex(0,1)
    I=np.matmul(Y,U)
    YII=np.zeros((len(innerbus),len(innerbus)))
    for i in range(0,len(innerbus)):
        for j in range(0,len(innerbus)):
            YII[i,j]=Y[innerbus[i]-1,innerbus[j]-1]
    YIB=np.zeros((len(innerbus),len(bordenbus)))
    for i in range((0,len(innerbus))):
        for j in range(0,len(bordenbus)):
            YIB[i,j]=Y[innerbus[i]-1,bordenbus[j]-1]
    YBI = np.zeros((len(bordenbus), len(innerbus)))
    for i in range((0, len(bordenbus))):
        for j in range(0, len(innerbus)):
            YBI[i, j] = Y[bordenbus[i]-1, innerbus[j]-1]
    YBB = np.zeros((len(bordenbus), len(bordenbus)))
    for i in range((0, len(bordenbus))):
        for j in range(0, len(bordenbus)):
            YBB[i, j] = Y[bordenbus[i]-1, bordenbus[j]-1]
    YBE = np.zeros((len(bordenbus), len(throwbus)))
    for i in range((0, len(bordenbus))):
        for j in range(0, len(throwbus)):
            YBE[i, j] = Y[bordenbus[i]-1, throwbus[j]-1]
    YEB = np.zeros((len(throwbus), len(bordenbus)))
    for i in range((0, len(throwbus))):
        for j in range(0, len(bordenbus)):
            YEB[i, j] = Y[throwbus[i] - 1, bordenbus[j] - 1]
    YEE = np.zeros((len(throwbus), len(throwbus)))
    for i in range((0, len(throwbus))):
        for j in range(0, len(throwbus)):
            YEE[i, j] = Y[throwbus[i] - 1, throwbus[j] - 1]
    YBBnew=YBB-np.matmul(np.matmul(YBE,np.linalg.inv(YEE)),YEB)
    IB=np.zeros(len(bordenbus))
    for i in range(0,len(bordenbus)):
        IB[i]=I[bordenbus[i]-1]
    IE = np.zeros(len(throwbus))
    for i in range(0, len(throwbus)):
        IE[i] = I[throwbus[i] - 1]
    IBnew=IB-np.matmul(np.matmul(YBE,np.linalg.inv(YEE)),YEB)