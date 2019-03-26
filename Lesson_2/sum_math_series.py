#-------------------------------------------------------------------------------
# Name:        sum_math_series
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#
# Author:      Fujitsu
#
# Created:     16.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input('Введите количество чисел в ряду:'))
elem = 1
s = 0
for i in range(n):
    s += elem
    elem /= -2
print('Сумма элементов ряда равна:', s)