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

#Находим макс. элемент среди мин. элементов столбцов
#Кол-во столбцов и строк вводит пользователь

from random import random
col = int(input())
row = int(input())
a = []
for i in range(row):
    b = []
    for j in range(col):
        n = int(random()*200)
        b.append(n)
        print('|{:4d}|'.format(n),end='')
    a.append(b)
    print()

max_elem = -1
for j in range(col):
    min_elem = 200
    for i in range(row):
        if a[i][j] < min_elem:
            min_elem = a[i][j]
    if min_elem > max_elem:
        max_elem = min_elem
print("Максимальный среди минимальных: ", max_elem)