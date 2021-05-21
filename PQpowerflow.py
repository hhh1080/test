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
    Ytt=Ycom
    Yft=-1*Ycom/Branchtap
    Ytf=-1*Ycom/Branchtap
    Yff=Ycom/Branchtap/Branchtap
    Ytt=Ytt+complex(0,1)*BranchB
    Yff=Yff+complex(0,1)*BranchB
    I=np.zeros(branchnum)
    for i in range(0,branchnum):
        I[i]=i
    Cf=csr_matrix((one,(Branch1-one,I)),shape=(busnum,branchnum),dtype=complex)
    Ct=csr_matrix((one,(Branch2-one,I)),shape=(busnum,branchnum),dtype=complex)
    CF=Cf.toarray()
    CT=Ct.toarray()
    Y=np.matmul(np.matmul(CF,np.diag(Yff)),CF.T)+np.matmul(np.matmul(CF,np.diag(Yft)),CT.T)\
      +np.matmul(np.matmul(CT,np.diag(Ytf)),CF.T)+np.matmul(np.matmul(CT,np.diag(Ytt)),CT.T)
    print(type(Y))
    print(Y)
    return Y

def PQflow(Y,Bus,busnum):
    Pgen=Bus[:,6]
    Pload=Bus[:,4]
    Qgen=Bus[:,7]
    Qload=Bus[:,5]
    Pi=Pgen-Pload
    Qi=Qgen-Qload
    for i in range(0,busnum):
        if Bus[i,1] == 3:
            Num=Bus[i,0]
    v=np.ones((busnum,1))
    o=np.zeros((busnum,1))
    for i in range(0,busnum):
        if Bus[i,1] == 2:
            v[i,0]=Bus[i,2]
    U=v*np.cos(o)+v*np.sin(o)*complex(0,1)
    Si=U*np.conjugate(np.matmul(Y,U))
    Pis=Si.real
    Qis=Si.imag
    deltaP=Pi-Pis
    deltaQ=Qi-Qis
    deltaP=np.delete(deltaP,Num-1,axis=0)
    U=np.delete(U,Num-1,axis=0)

    deltaPU=deltaP/U


Y=YData()