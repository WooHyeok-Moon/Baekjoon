import sys
A,B=1,1

while 1:
    A,B=map(int,sys.stdin.readline().split())
    if (A,B)==(0,0):
        break
    print(A+B)
