import sys
import test_1
import numpy as np

def collatz(number):
    if number%2 == 0:
        w=number/2
        print(w)
    if number%2 == 1:
        w=3*number+1
        print(w)
    return w

aa=np.array([[1,2,3],[2,3,4],[3,4,5]])
b=aa[:,0]
c=2*aa[:,1]
print(type(b))
print(b)
print(b+c)
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



