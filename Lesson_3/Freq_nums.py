#-------------------------------------------------------------------------------
# Name:        freq_num
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yuri Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Находим наиболее часто встречающееся число в массиве случайных чисел.
#Размер массива задает пользователь

from random import random
N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 50)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')