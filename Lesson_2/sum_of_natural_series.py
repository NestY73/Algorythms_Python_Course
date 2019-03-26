#-------------------------------------------------------------------------------
# Name:        sum_of_natural_series
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     26.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input())
s = 0
for i in range(1,n+1):
    s += i
s1 = n * (n + 1) // 2

print('Число в левой части выражение равно: {:d}'.format(s))
print('Число в правой части выражение равно: {:d}'.format(s1))
if s == s1:
    print("Тождество доказано")
