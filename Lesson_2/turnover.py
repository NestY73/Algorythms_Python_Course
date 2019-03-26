#-------------------------------------------------------------------------------
# Name:        turnover
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# 1 способ

n1 = input("Введите целое число: ")
n2 = ''

n2 = n1[::-1]

print('"Обратное" ему число:',n2)


# 2 способ

n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:
    n2 = n2 * 10 + n1 % 10;
    n1 = n1 // 10

print('"Обратное" ему число:',n2)
