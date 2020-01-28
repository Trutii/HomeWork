from random import *
a=[[randint(0,255) for i in range(4)] for j in range(3)]
max_a=a[0][0]
for i in range(3):
    for j in range(4):
        print("{:3d}".format(a[i][j]),end=" ")
    print()
s=0
for i in range(3):
    for j in range(4):
        s+=a[i][j]
s=s/12
print(s)
for i in range(3):
    for j in range(4):
        if a[i][j]>s:
            a[i][j]=255
        else:
            a[i][j]=0
for i in range(3):
    for j in range(4):
        print("{:3d}".format(a[i][j]),end=" ")
    print()
