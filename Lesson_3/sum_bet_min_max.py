#-------------------------------------------------------------------------------
# Name:        sum_between_max_min
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yuri Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Находим сумму элементов между макс. и мин. элементами массива

from random import random

N = int(input())
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('{:3d}'.format(a[i]), end='')
print()

min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print('Мин. элемент: {:d} Макс. элемент: {:d}'.format(a[min_id], a[max_id]))

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print('Сумма между мин. и максимальным эелементами массива: ',summa)