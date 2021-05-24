import numpy as np
import re
import math
import readIEEEfile as read
from scipy.sparse import csr_matrix

def YData():
    busnum,Bus=read.BusData()
    branchnum,Branch=read.BranchData(busnum)
    Branch1=Branch[:,0]
    Branch2=Branch[:,1]
    BranchR=Branch[:,2]
    BranchX=Branch[:,3]
    BranchB=Branch[:,4]
    Branchtap=Branch[:,5]
    for i in range(0,branchnum):
        if Branchtap[i] == 0:
            Branchtap[i] = 1
    one=np.ones(branchnum)
    Ycom = one/(BranchR + complex(0,1)*BranchX)
    # Ycom = one / (BranchR + complex(0, 1) * BranchX) + complex(0,1)*BranchB
    Ytt=Ycom
    Yft=-1*Ycom*Branchtap
    Ytf=-1*Ycom*Branchtap
    Yff=Ycom*Branchtap*Branchtap
    Ytt=Ytt+complex(0,1)*BranchB
    Yff=Yff+complex(0,1)*BranchB
    I=np.zeros(branchnum)
    # for i in range(0,branchnum):
    #     I[i]=i
    # Cf=csr_matrix((one,(Branch2-one,I)),shape=(busnum,branchnum),dtype=complex)
    # Ct=csr_matrix((one,(Branch1-one,I)),shape=(busnum,branchnum),dtype=complex)
    # CF=Cf.toarray()
    # CT=Ct.toarray()
    # Y=np.matmul(np.matmul(CF,np.diag(Yff)),CF.T)+np.matmul(np.matmul(CF,np.diag(Yft)),CT.T)\
    #   +np.matmul(np.matmul(CT,np.diag(Ytf)),CF.T)+np.matmul(np.matmul(CT,np.diag(Ytt)),CT.T)
    Y=np.zeros((busnum,busnum),dtype=complex)
    for i in range(0,branchnum):
        Y[int(Branch1[i]-1),int(Branch1[i]-1)]+=Ytt[i]
        Y[int(Branch1[i]-1),int(Branch2[i]-1)]+=Ytf[i]
        Y[int(Branch2[i]-1),int(Branch1[i]-1)]+=Yft[i]
        Y[int(Branch2[i]-1),int(Branch2[i]-1)]+=Yff[i]
    # for i in range(0,busnum):
    #     for j in range(0,busnum):
    #         Y[i][j]=Y[i][j]+Bus[i][9]
    for i in range(0,busnum):
        Y[i][i]+=complex(0,1)*Bus[i][9]
    # print(type(Y))
    # print(Y)
    # print(Bus)
    return Y,Bus,busnum

def PQflow(Y,Bus,busnum):
    PQNum=0
    Pgen=Bus[:,6];Pgen=Pgen.reshape(busnum,1)
    Pload=Bus[:,4];Pload=Pload.reshape(busnum,1)
    Qgen=Bus[:,7];Qgen=Qgen.reshape(busnum,1)
    Qload=Bus[:,5];Qload=Qload.reshape(busnum,1)
    Pi=Pgen-Pload
    Pi=Pi/100
    Qi=Qgen-Qload
    Qi=Qi/100
    pbus=[]
    pvbus=[]
    for i in range(0,busnum):
        if Bus[i,1] == 3:
            pbus.append(int(Bus[i,0]-1))
    for i in range(0,busnum):
        if Bus[i,1] !=0:
            pvbus.append(int(Bus[i,0]-1))
    v=np.ones((busnum,1))
    o=np.zeros((busnum,1))
    for i in range(0,busnum):
        if Bus[i,1] == 2:
            v[i,0]=Bus[i,2]
        if Bus[i,1] == 3:
            v[i,0]=Bus[i,2]
    pbus=np.array(pbus)
    pvbus=np.array(pvbus)
    B = Y.imag
    B1 = np.delete(B, pbus, axis=0)
    B1 = np.delete(B1, pbus, axis=1)
    B2 = np.delete(B, pvbus, axis=0)
    B2 = np.delete(B2, pvbus, axis=1)
    threshold=0.00001
    while True:
        U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
        Si = U * np.conjugate(np.matmul(Y, U))
        Pis = Si.real
        # Qis=Si.imag
        # deltaP=np.zeros((busnum,1))
        deltaP = Pi - Pis
        # deltaQ=Qi-Qis
        deltaP = np.delete(deltaP, pbus, axis=0)
        U1 = np.delete(v, pbus, axis=0)
        # deltaQ=np.delete(deltaQ,pvbus,axis=0)
        # U2=np.delete(U,pvbus,axis=0)
        deltaPU = deltaP / U1
        # Ua = -1 * np.matmul(np.linalg.inv(B1), deltaPU)
        Ua=np.linalg.solve(-B1,deltaPU)
        dangle = Ua / U1
        d=0
        for i in range(0,len(o)):
            if Bus[i,1] !=3:
                o[i]=o[i]+dangle[d]
                d=d+1
        if np.max(deltaP)>threshold:
            kp=0
        else:
            kp=1
            if kq == 1:
                print(PQNum)
                break
        U = v * np.cos(o) + v * np.sin(o) * complex(0, 1)
        Si = U * np.conjugate(np.matmul(Y, U))
        Qis = Si.imag
        # deltaQ = np.zeros((busnum, 1))
        deltaQ = Qi - Qis
        deltaQ = np.delete(deltaQ, pvbus, axis=0)
        U2 = np.delete(v, pvbus, axis=0)
        deltaQU = deltaQ / U2
        # dU = -1 * np.matmul(np.linalg.inv(B2), deltaQU)
        dU=-1*np.linalg.solve(B2,deltaQU)
        d=0
        for i in range(0,len(v)):
            if Bus[i,1] == 0:
                v[i]=v[i]+dU[d]
                d=d+1
        if np.max(deltaQ)>threshold:
            kq=0
        else:
            kq=1
            if kp == 1:
                print(PQNum)
                break
        PQNum = PQNum + 1
        if PQNum > 100:
            print("The load flow does not converge")
            break
    o=o*180/math.pi
    return v,o

