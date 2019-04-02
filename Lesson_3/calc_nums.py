#-------------------------------------------------------------------------------
# Name:        calm_num
# Purpose:     Homework - Lesson 3_Algorythms
#
# Author:      Yury Nesterovich
#
# Created:     31.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Находим количество чисел  кратных от 2 до 9 в первой 1000
a = [0]*8
for i in range(2,1000):
    for j in range(2,10):
        if i % j == 0:
            a[j-2] += 1

print('Среди чисел до 1000:')
i = 0
while i < len(a):
    print('Кратно ',i+2, ' - ', a[i], 'чисел')
    i += 1
