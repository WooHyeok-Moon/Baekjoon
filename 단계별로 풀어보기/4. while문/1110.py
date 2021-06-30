import sys

N=int(sys.stdin.readline())
len_N=0

if N<10:
    sum_N='0'+str(N)
else:
    sum_N=str(N)

while 1:
    len_N+=1
        
    if int(sum_N[0])+int(sum_N[1])<10:
        sum_N = sum_N[1] + str(int(sum_N[0])+int(sum_N[1]))

    else:
        sum_N= sum_N[1] + str(int(sum_N[0])+int(sum_N[1]))[1]

    if int(sum_N)==N:
        print(len_N)
        break
    if len(sum_N)==1:
        sum_N='0'+str(sum_N)
