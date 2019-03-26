#-------------------------------------------------------------------------------
# Name:        qty_digits
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     26.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input("Количество вводимых чисел? "))
d = int(input("Какую цифру будем считать? "))
count = 0
for i in range(1,n+1):
    m = int(input("Число " + str(i) + ": "))
    print("Введено число: {:d}".format(m))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено {:d} цифр {:d}".format(count, d))