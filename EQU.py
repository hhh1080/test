import math
import numpy as np

def Ward(savebus,allbus,Y,v,o):
    allbus1=allbus.tolist() #得到所有节点
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

def Ward1(savebus,allbus,Y,v,o,Bus):
    allbus1 = allbus.tolist()  # 得到所有节点
    savebus1 = savebus.tolist()
    throwbus1 = list(set(allbus1).difference(set(savebus1)))
    throwbus = np.array(throwbus1,dtype=int)
    one = np.ones((len(throwbus)), dtype=int)
    U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
    I = np.matmul(Y, U)
    bordenbus = [];
    bordenv = []
    for i in range(0, len(savebus)):
        for j in range(0, len(throwbus)):
            if Y[int(savebus[i] - 1), int(throwbus[j] - 1)] != 0:
                bordenbus.append(int(savebus[i]))
                bordenv.append(U[int(savebus[i] - 1)])
                break
    # bordenbus=np.array(bordenbus)
    # innerbus1=[]
    innerbus1 = list(set(savebus1).difference(set(bordenbus)))
    bordenbus = np.array(bordenbus)
    bordenv = np.array(bordenv)
    bordenv = bordenv.reshape(len(bordenbus), 1)
    innerbus = np.array(innerbus1)
    YII = np.zeros((len(innerbus), len(innerbus)), dtype=complex)
    for i in range(0, len(innerbus)):
        for j in range(0, len(innerbus)):
            YII[i, j] = Y[int(innerbus[i] - 1), int(innerbus[j] - 1)]
    YIB = np.zeros((len(innerbus), len(bordenbus)), dtype=complex)
    for i in range(0, len(innerbus)):
        for j in range(0, len(bordenbus)):
            YIB[i, j] = Y[int(innerbus[i] - 1), int(bordenbus[j] - 1)]
    YBI = np.zeros((len(bordenbus), len(innerbus)), dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(innerbus)):
            YBI[i, j] = Y[int(bordenbus[i] - 1), int(innerbus[j] - 1)]
    YBB = np.zeros((len(bordenbus), len(bordenbus)), dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(bordenbus)):
            YBB[i, j] = Y[int(bordenbus[i] - 1), int(bordenbus[j] - 1)]
    YBE = np.zeros((len(bordenbus), len(throwbus)), dtype=complex)
    for i in range(0, len(bordenbus)):
        for j in range(0, len(throwbus)):
            YBE[i, j] = Y[int(bordenbus[i] - 1), int(throwbus[j] - 1)]
    YEB = np.zeros((len(throwbus), len(bordenbus)), dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(bordenbus)):
            YEB[i, j] = Y[int(throwbus[i] - 1), int(bordenbus[j] - 1)]
    YEE = np.zeros((len(throwbus), len(throwbus)), dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(throwbus)):
            YEE[i, j] = Y[int(throwbus[i] - 1), int(throwbus[j] - 1)]
    YBBnew = YBB - np.matmul(np.matmul(YBE, np.linalg.inv(YEE)), YEB)
    # IB = np.zeros((len(bordenbus), 1), dtype=complex)
    # II = np.zeros((len(innerbus), 1), dtype=complex)
    # for i in range(0, len(bordenbus)):
    #     IB[i][0] = I[int(bordenbus[i] - 1)][0]
    # for i in range(0, len(innerbus)):
    #     II[i][0] = I[int(innerbus[i] - 1)][0]
    # IE = np.zeros((len(throwbus), 1), dtype=complex)
    # for i in range(0, len(throwbus)):
    #     IE[i][0] = I[int(throwbus[i] - 1)][0]
    # IBnew = IB - np.matmul(np.matmul(YBE, np.linalg.inv(YEE)), IE)
    invYEE = np.linalg.inv(YEE)
    # sEQ = bordenv * np.conjugate(np.matmul(np.matmul(YBE, invYEE), IE))
    # PEQ = sEQ.real
    # QEQ = sEQ.imag
    conbordenv=np.conjugate(bordenv)
    conbordenv=conbordenv.flatten()
    diagvb=np.diag(conbordenv)
    PE= np.zeros((len(throwbus), 1))
    QE = np.zeros((len(throwbus), 1))
    for i in range(0, len(throwbus)):
        PE[i][0] = Bus[int(throwbus[i] - 1)][4] / 100
        QE[i][0] = Bus[int(throwbus[i] - 1)][5] / 100
    SE = PE + complex(0, 1) * QE
    throwv=U[throwbus-one]
    throwv=throwv.reshape(len(throwbus),1)
    IE=np.conjugate(SE/throwv)
    Y1=np.matmul(np.matmul(diagvb,YBE),invYEE)
    deltaSB=np.matmul(Y1,IE)
    for i in range(0,len(bordenbus)):
        Bus[int(bordenbus[i]-1)][4]-=deltaSB[i].real*100
        Bus[int(bordenbus[i]-1)][5]-=deltaSB[i].imag*100
    # Bus1=np.zeros((len(savebus),12))
    onebor = np.ones((len(bordenbus)), dtype=int)
    oneinn = np.ones((len(innerbus)), dtype=int)
    Bus1=Bus[bordenbus-onebor]
    Bus2=Bus[innerbus-oneinn]
    Busnew=np.concatenate((Bus1,Bus2),axis=0)
    for i in range(0,len(savebus)):
        Busnew[i][0]=i
    Y11=np.concatenate((YBBnew,YBI),axis=1)
    Y22=np.concatenate((YIB,YII),axis=1)
    Ynew=np.concatenate((Y11,Y22),axis=0)
    return throwbus, bordenbus, innerbus, Busnew,Ynew

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

def GenGroup1(group,Bus,v,o,Y):
    allbus = Bus[:, 0] #全部原始节点
    groupnum = group.shape[0] #第i组下发电机数量
    for i in range(0,groupnum):
        equbus = Bus.shape[0] + i #得到新的节点号
        group1 = group[i, :] #第i组的发电机节点号
        group1=np.array(group1)
        equv = 0
        equa = 0
        for j in range(0,len(group1)): #求得每个发电机的电压之和与角度之和
            equv+=v[int(group1[j]-1)]
            equa += o[int(group1[j] - 1)]
        equv=equv/len(group1) #平均值求新节点电压幅值
        equa=equa/len(group1) #平均值求新节点角度
        avrvU=equv*np.cos(equa)+equv*complex(0,1)*np.sin(equa) #求得新节点电压的复数量
        U = v * np.cos(o) + v * np.sin(o) * complex(0, 1) #求得目前各节点电压复数量数组
        originbus = [] #存放关联节点的列表
        for a in range(0, len(allbus)):
            for b in range(0, len(group1)):
                if allbus[a] in group1:
                    break
                if Y[int(allbus[a] - 1), int(group1[b] - 1)] != 0:
                    originbus.append(int(allbus[a]))
                    break
        Ugen = [] #存放原始发电机节点的电压复数量
        for x in range(0, len(group1)):
            Ugen.append(U[int(group1[x] - 1)])
        Ugen=np.array(Ugen);Ugen=Ugen.reshape(len(group1),1)
        ak=Ugen/avrvU #移相器复变比的矩阵
        yk0=np.zeros((len(group1),1))
        for a in range(0,len(group1)): #消去同调母线间的关联支路
            for b in range(0,len(group1)):
                if a<=b:
                    break
                if Y[int(group1[a]-1)][int(group1[b]-1)] !=0: #计算母线关联支路等值到各发电机节点的对地导纳
                    yk0[int(group1[a]-1)]+=1-U[int(group1[b]-1)]/U[int(group1[a]-1)]*Y[int(group1[a]-1)][int(group1[b]-1)]*-1
                    yk0[int(group1[b]-1)]+=1-U[int(group1[a]-1)]/U[int(group1[b]-1)]*Y[int(group1[a]-1)][int(group1[b]-1)]*-1
        akyk0=abs(ak)*abs(ak)*yk0
        yt0=np.sum(akyk0) #将等值对地支路全转化为新节点的对地支路
        Y12 = np.zeros((len(originbus), len(group1)),dtype=complex)
        Uorigin=[]
        for a in range(0, len(originbus)): #找出原始发电机节点与系统相连的内部节点之间的导纳
            for b in range(0, len(group1)):
                Y12[a][b] = -Y[int(originbus[a]-1), int(group1[b]-1)]
            Uorigin.append(U[int(originbus[a]-1)]) #提取出内部相关节点的电压
        Uorigin = np.array(Uorigin);Uorigin = Uorigin.reshape(len(originbus), 1)
        #计算移相器对内部节点侧的对地支路的影响
        Yorigin0 = avrvU/Uorigin * np.matmul(Y12, abs(ak) - abs(ak) * (np.cos(np.arctan(ak.imag / ak.real)) + complex(0, 1) * np.sin(np.arctan(ak.imag / ak.real))))
        #计算移相器对新节点的对地支路的影响
        Yt0=Uorigin/avrvU*np.matmul(Y12,abs(ak)-abs(ak)*(np.cos(np.arctan(ak.imag/ak.real))-complex(0,1)*np.sin(np.arctan(ak.imag/ak.real))))
        Yt00=np.sum(Yt0)
        akabs2=abs(ak)*abs(ak)
        Ytt=np.sum(np.matmul(Y12,akabs2)) #计算网络化简后新支路对新节点的自导纳的影响

        Y = np.append(Y, np.zeros((1, Y.shape[1])), axis=0) #加上新节点的导纳部分
        Y = np.append(Y, np.zeros((Y.shape[0], 1)), axis=1)
        t = Y.shape[0] - 1
        YRC = -np.matmul(Y12, abs(ak)) #内部节点对新节点的互导纳
        # sumY12=np.sum(Y12,axis=1)
        for a in range(0, len(originbus)):
            Y[int(originbus[a]) - 1][t] = YRC[a][0] #加上新支路上的互导纳
            Y[t][int(originbus[a]) - 1] = YRC[a][0]
            # Y[int(originbus[a]) - 1][int(originbus[a]) - 1] -=sumY12[a] #减去原始线路上内部节点的自导纳（错误）
            Y[int(originbus[a]) - 1][int(originbus[a]) - 1] += Yorigin0[a][0] #内部节点加上新的自导纳
        Y[t][t] =Y[t][t]+Ytt+Yt00+yt0 #新节点的自导纳
        one = np.ones((len(group1)))
        Y = np.delete(Y, group1 - one, axis=0)  # 消去原始发电机节点的导纳部分
        Y = np.delete(Y, group1 - one, axis=1)

        #由于一般消去的发电机都是PV节点，因此有功功率,无功功率应该可以直接相加
        Ptgen=0;Qtgen=0;Pload=0;Qload=0
        for a in range(0,len(group1)):
            Ptgen+=Bus[int(group1[a]-1)][6]
            Qtgen += Bus[int(group1[a] - 1)][7]
            Pload+=Bus[int(group1[a]-1)][4]
            Qload+=Bus[int(group1[a]-1)][5]

        Bus=np.append(Bus,np.zeros((1, Bus.shape[1])),axis=0)
        Bus[t][0]=equbus;Bus[t][1]=2;Bus[t][2]=equv;Bus[t][3]=equa;Bus[t][4]=Pload;Bus[t][5]=Qload;Bus[t][6]=Ptgen;Bus[t][7]=Qtgen;Bus[t][9]=(Yt00+yt0).imag
        Bus = np.delete(Bus, group1 - one, axis=0)  # 消去原始发电机节点的信息
        for x in range(0,Bus.shape[0]):
            Bus[x][0]=x+1
        return Bus,Y

def CSR(Y,throwbus,allbus,v,o,Bus):
    allbus1=allbus.tolist()
    throwbus1=throwbus.tolist()
    savebus = list(set(allbus1).difference(set(throwbus1))) #得到保留节点
    savebus = np.array(savebus)
    Y11 = np.zeros((len(savebus), len(savebus)), dtype=complex)
    for i in range(0,len(savebus)):
        for j in range(0,len(savebus)):
            Y11[i,j]=Y[int(savebus[i]-1),int(savebus[j]-1)]
    Y12 = np.zeros((len(savebus), len(throwbus)), dtype=complex)
    for i in range(0, len(savebus)):
        for j in range(0, len(throwbus)):
            Y12[i, j] = Y[int(savebus[i] - 1), int(throwbus[j] - 1)]
    Y21 = np.zeros((len(throwbus), len(savebus)), dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(savebus)):
            Y21[i, j] = Y[int(throwbus[i] - 1), int(savebus[j] - 1)]
    Y22 = np.zeros((len(throwbus), len(throwbus)), dtype=complex)
    for i in range(0, len(throwbus)):
        for j in range(0, len(throwbus)):
            Y22[i, j] = Y[int(throwbus[i] - 1), int(throwbus[j] - 1)]
    U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
    U1=np.zeros((len(savebus),1)) #保留节点的电压复数量
    for i in range(0,len(savebus)):
        U1=U[int(savebus[i]-1)][0]
    U2 = np.zeros((len(throwbus), 1)) #消去节点的电压复数量
    for i in range(0, len(throwbus)):
        U2 = U[int(throwbus[i] - 1)][0]
    #目前先考虑全为恒阻抗的情况，如果某节点有恒阻抗负载，相当于该节点对地导纳增加了该恒阻抗
    # P=np.zeros((len(throwbus),1))
    # Q = np.zeros((len(throwbus), 1))
    # for i in range(0,len(throwbus)):
    #     P[i][0]=Bus[int(throwbus[i]-1)][4]/100
    #     Q[i][0]=Bus[int(throwbus[i]-1)][5]/100
    # S=P+complex(0,1)*Q
    # y22=np.conjugate(S/abs(U2)/abs(U2))
    # y220=y22.flatten()
    # Y220=np.diag(y220)
    # Y22+=Y220
    # Y11new=Y11-np.matmul(np.matmul(Y12,np.linalg.inv(Y22)),Y21)
    # one=np.ones((len(throwbus)))
    # Bus = np.delete(Bus, throwbus - one, axis=0)  # 消去原始发电机节点的信息
    # for i in range(0,len(savebus)):
    #     Bus[i][0]=i+1
    #该板块下考虑50%的恒阻抗与50%的恒功率模型
    P = np.zeros((len(throwbus), 1))
    Q = np.zeros((len(throwbus), 1))
    for i in range(0, len(throwbus)):
        P[i][0] = Bus[int(throwbus[i] - 1)][4] / 100
        Q[i][0] = Bus[int(throwbus[i] - 1)][5] / 100
    #此处为恒阻抗处理部分
    Pz=P*1
    Qz=Q*1
    Sz = Pz + complex(0, 1) * Qz
    y22 = np.conjugate(Sz / abs(U2) / abs(U2))
    y220 = y22.flatten()
    Y220 = np.diag(y220)
    Y22 += Y220
    Y11new = Y11 - np.matmul(np.matmul(Y12, np.linalg.inv(Y22)), Y21)
    #移植到保留节点上的
    #此处为恒功率处理部分（由于是静态潮流
    Ps = P*0
    Qs = Q*0
    Ss = Ps + complex(0, 1) * Qs
    Is=np.conjugate(Ss/U2)
    Isnew=-np.matmul(np.matmul(Y12,np.linalg.inv(Y22)),Is)
    #保留节点上的功率增量
    deltaSs=U1*np.conjugate(Isnew)
    deltaPs=deltaSs.real
    deltaQs=deltaSs.imag
    for i in range(0,len(savebus)):
        Bus[int(savebus[i] - 1)][4] += deltaPs[i][0] * 100
        Bus[int(savebus[i] - 1)][5] += deltaQs[i][0] * 100
    one=np.ones((len(throwbus)),dtype=int)
    Bus = np.delete(Bus, throwbus - one, axis=0)  # 消去原始发电机节点的信息
    for i in range(0, len(savebus)):
        Bus[i][0] = i + 1
    return Y11new,Bus

