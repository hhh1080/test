import math
import numpy as np

def Ward(savebus,allbus,Y,v,o):
    allbus1=allbus.tolist()
    savebus1=savebus.tolist()
    throwbus1=list(set(allbus1).difference(set(savebus1)))
    throwbus=np.array(throwbus1)
    U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
    I = np.matmul(Y, U)
    bordenbus=[];bordenv=[]
    for i in range(0,len(savebus)):
        for j in range(0,len(throwbus)):
            if Y[int(savebus[i]-1),int(throwbus[j]-1)] != 0:
                bordenbus.append(int(savebus[i]))
                bordenv.append(U[int(savebus[i]-1)])
                break
    # bordenbus=np.array(bordenbus)
    # innerbus1=[]
    innerbus1=list(set(savebus1).difference(set(bordenbus)))
    bordenbus = np.array(bordenbus);bordenv=np.array(bordenv);bordenv=bordenv.reshape(len(bordenbus),1)
    innerbus=np.array(innerbus1)
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
    invYEE=np.linalg.inv(YEE)
    sEQ=bordenv*np.conjugate(np.matmul(np.matmul(YBE,invYEE),IE))
    PEQ=sEQ.real
    QEQ=sEQ.imag
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

def GenGroup(group,Bus,v,o,Y):
    allbus=Bus[:,0]
    groupnum=group.shape[0]
    for i in range(0,groupnum):
        equbus=Bus.shape[0]+i
        group1=group[i,:]
        equv=0
        equa=0
        for j in range(0,len(group1)):
            equv+=v[int(group1[j]-1)]
            equa += o[int(group1[j] - 1)]
        equv=equv/len(group1)
        equa=equa/len(group1)
        avrvU=equv*np.cos(equa)+equv*complex(0,1)*np.sin(equa)
        U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
        rbus=[]
        for a in range(0, len(allbus)):
            for b in range(0, len(group1)):
                if allbus[a] in group1:
                    break
                if Y[int(allbus[a] - 1), int(group1[b] - 1)] != 0:
                    rbus.append(int(allbus[a]))
                    break
        U1=[];U2=[];U2abs=[]
        for x in range(0, len(rbus)):
            U1.append(U[int(rbus[x]-1)])
        for x in range(0,len(group1)):
            U2.append(U[int(group1[x]-1)])
            U2abs.append(v[int(group1[x]-1)])
        U1=np.array(U1);U1=U1.reshape(len(rbus),1)
        U2=np.array(U2);U2=U2.reshape(len(group1),1)
        U2abs=np.array(U2abs);U2abs=U2abs.reshape(len(group1),1)
        Y12equ=np.zeros((len(rbus),len(group1)))
        Y12=np.zeros((len(rbus),len(group1)))
        for a in range(0,len(rbus)):
            for b in range(0,len(group1)):
                Y12equ[a][b]=Y[int(rbus[a]),int(group1[b])]*v[int(group1[b]-1)]/equv
                Y12[a][b]=Y[int(rbus[a]),int(group1[b])]
        # Y22=np.zeros((len(group1),len(group1)))
        Y22=0
        for a in range(0,len(group1)):
            # Y22[a][a]=Y[int(group1[a]-1),int(group1[a]-1)]*v[int(group1[a]-1)]*v[int(group1[a]-1)]/equv/equv
            Y22 += Y[int(group1[a] - 1), int(group1[a] - 1)] * v[int(group1[a] - 1)] * v[int(group1[a] - 1)] / equv / equv
        Ut=U2/avrvU
        Ur=U2abs/equv
        akabs=U2abs/equv
        y10=avrvU/U1*np.matmul(Y12,akabs-akabs*(np.cos(np.arctan(Ut.imag/Ut.real))+complex(0,1)*np.sin(np.arctan(Ut.imag/Ut.real))))
        y20=U1/avrvU*np.matmul(Y12,akabs-akabs*(np.cos(np.arctan(Ut.imag/Ut.real))-complex(0,1)*np.sin(np.arctan(Ut.imag/Ut.real))))
        Y22+=y20

        group1=np.array(group1)
        Y=np.delete(Y,group1,axis=0)
        Y = np.delete(Y, group1, axis=1)
        Y=np.append(Y,np.zeros((1,Y.shape[1])),axis=0)
        Y = np.append(Y, np.zeros((Y.shape[0],1)), axis=1)
        t=Y.shape[0]-1
        YRC=np.matmul(Y12,Ur)
        for a in range(0,len(rbus)):
            Y[int(rbus[a])-1][t]=YRC[a][0]
            Y[t][int(rbus[a])-1]=YRC[a][0]
            Y[int(rbus[a])-1][int(rbus[a])-1]+=y10[a][0]
        Y[t][t]+=Y22