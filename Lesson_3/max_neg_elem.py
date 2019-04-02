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

# Находим максимальный отрицательный элемент массива и выводим его

from random import random
N = int(input())
arr = []
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1

print('Макс. отрицательный элемент: индекс {:d}, значение {:d}'.format(index+1, arr[index]))