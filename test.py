import sys
import test_1
import numpy as np
import math

def collatz(number):
    if number%2 == 0:
        w=number/2
        print(w)
    if number%2 == 1:
        w=3*number+1
        print(w)
    return w
cc=np.array([[1+1j,1+2j],[2+2j,2+3j]])
dd=cc.real
print(dd)
numtest=[]
numtest.append(1)
print(type(numtest))
print(numtest)
aa=np.array([[1,2,3],[2,3,4],[3,4,5]])
b=[3,4]
# c=[0,1]
# aa=np.delete(aa,b,axis=0)
# aa=np.delete(aa,b,axis=1)
bb=np.array([[3.6],[2.1],[-1.4]])
cc=np.array([[3,1,-1],[1,2,4],[-1,4,5]])
r=np.linalg.solve(cc,bb)
print('r=\n')
print(r)
while True:
    c = input()
    try:
        a = int(c)
    except ValueError:
        print("Please input a currect number")
        continue
    if a == 0:
        test_1.DisplayFcn()
        sys.exit()
    while True:
        b=collatz(a)
        a=b
        if b == 1:
            print("Caculation Finished")
            break



