from random import *
a=[[randint(0,100) for i in range(4)] for j in range(3)]
max_a=a[0][0]
for i in range(3):
    for j in range(4):
        print("{:3d}".format(a[i][j]),end=" ")
    print()
j_max=0
i_max=0
for i in range(3):
    for j in range(4):
        if a[i][j]>max_a:
            max_a=a[i][j]
            i_max=i
            j_max=j
min_a=a[0][0]
j_min=0
i_min=0
for i in range(3):
    for j in range(4):
        if a[i][j]<min_a:
            min_a=a[i][j]
            i_min=i
            j_min=j
print("Наибольший элемент a[{:d},{:d}]={:d}".format(i_max,j_max,max_a))
print("Наименьший элемент a[{:d},{:d}]={:d}".format(i_min,j_min,min_a))
