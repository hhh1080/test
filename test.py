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
dd=np.array([[1],[2],[3]])
ee=dd.flatten()
print('ee')
print(np.diag(ee))
# c=[0,1]
# aa=np.delete(aa,b,axis=0)
# aa=np.delete(aa,b,axis=1)
bb=np.array([[1],[2]])
cc=np.array([])
aa=[1,2,3]
for i in range(0,3):
    cc=np.append(cc,aa,axis=0)
print("cc")
print(cc)
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



