#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yuri Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Находим 2 наименьших элемента массива

from random import random
N = int(input())
a = []
for i in range(N):
    a.append(int(random()*100))
    print("{:3d}".format(a[i]), end='')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2,N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("Первый мин. элемент №{:3d}:{:3d}".format(min1+1, a[min1]))
print("Второй мин. элемент №{:3d}:{:3d}".format(min2+1, a[min2]))