#-------------------------------------------------------------------------------
# Name:        max_min_elem
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yuri Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#В массиве случайных целых чисел поменять местами
#минимальный и максимальный элементы массива, количество элементов
#задается пользователем. Элменты массива - случаные числа от 1 до 100

from random import random
N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100) + 1
    print(arr[i],end=' ')
print()

#### 1-й вариант, используем функции max и min
##min_elem = min(arr)
##max_elem = max(arr)
##ind_min = arr.index(min_elem)
##ind_max = arr.index(max_elem)
##print('Мин. элемент arr[{:d}] = {:d}, Макс. элемент arr[{:d}] = {:d}'.format(ind_min+1, min_elem, ind_max+1, max_elem))
##arr[ind_min],arr[ind_max] = arr[ind_max],arr[ind_min]
##
##for i in range(N):
##    print(arr[i],end=' ')
##print()
#####

# 2-й вариант метод перебора элементов и поиска макс и мин.
min_elem = arr[0]
max_elem = arr[0]
ind_min = 0
ind_max = 0
for i in range(N):
    if arr[i] < arr[ind_min]:
        min_elem = arr[i]
        ind_min = i
    elif arr[i] > arr[ind_max]:
        max_elem = arr[i]
        ind_max = i
print('Мин. элемент arr[{:d}] = {:d}, Макс. элемент arr[{:d}] = {:d}'.format(ind_min+1, min_elem, ind_max+1, max_elem))
elem = arr[ind_min]
arr[ind_min] = arr[ind_max]
arr[ind_max] = elem
for i in range(N):
    print(arr[i],end=' ')
print()
