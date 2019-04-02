#-------------------------------------------------------------------------------
# Name:        index_even_array_elem
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yuri Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Находим индексы четных элементов массива. Массив состоит из 15 элементов,
#которые заполнены случаными элементами от 0 до 100

from random import random
N = 15
elem_array = [0]*N
even = []
for i in range(N):
    elem_array[i] = int(random() * 100)+1
    if elem_array[i] % 2 == 0:
        even.append(i)
    print(elem_array[i], end=' ')
print()
print('Индексы четных элементов:')
for elem in even:
    print(elem, end=' ')
