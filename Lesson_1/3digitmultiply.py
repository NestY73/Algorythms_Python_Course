#-------------------------------------------------------------------------------
# Name:        3digitmultiply
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

s = input("Введите число:")
sum = 0
mul = 1
i = 0
while i < len(s):
    sum += int(s[i])
    mul *= int(s[i])
    i += 1
print(sum)
print(mul)