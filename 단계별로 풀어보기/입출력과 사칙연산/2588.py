import sys

num1,num2=[],[]

num1,num2=[sys.stdin.readline().strip() for i in range(2)]

op=[(str(int(num2[2-i])*int(num1[2-x]))) for i in range(3) for x in range(3)]
res1=str(int(op[0])+int(op[1]+'0')+int(op[2]+'00'))
res2=str(int(op[3])+int(op[4]+'0')+int(op[5]+'00'))
res3=str(int(op[6])+int(op[7]+'0')+int(op[8]+'00'))
res4=str(int(res1)+int(res2+'0')+int(res3+'00'))

print(res1)
print(res2)
print(res3)
print(res4)