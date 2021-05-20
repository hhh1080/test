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
    YY = np.zeros((busnum, busnum))
    # Y = np.array(YY, dtype=complex)
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
    print(type(CF))
    print(CF)

YData()