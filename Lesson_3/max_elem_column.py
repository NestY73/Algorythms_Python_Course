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

# Заполняем матрицу с клавиатуры и считаем сумму элементов строки.
# Выводим новую матрицу


row = 5
col = 4
a = []
for i in range(col):
    b = []
    s = 0
    print("{:d}-я строка:".format(i))
    for j in range(row-1):
        n = int(input())
        s += n
        b.append(n)
    print(b)
    b.append(s)
    a.append(b)
print()
print('Матрица с суммой элементов строки в последнем столбце')
for i in a:
    print(i)

