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
n=np.arange(7)
print('n')
print(n)
# c=[0,1]
# aa=np.delete(aa,b,axis=0)
# aa=np.delete(aa,b,axis=1)
a='L PUBGSHI 500.'
a=a.encode('utf-8')
a=a.decode('utf-8')
if a[0:2] == 'L ':
    print("YYY")
else:print("NNN")
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



