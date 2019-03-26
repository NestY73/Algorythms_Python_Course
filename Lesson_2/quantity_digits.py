#-------------------------------------------------------------------------------
# Name:        even_odd_calc
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# 1 вариант решения:
a = int(input("Введите число:"))

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Even: %d, odd: %d" % (even, odd))


# 2 вариант решения:

num = input("Введите число:")
even = 0
odd = 0

for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even: %d, odd: %d" % (even, odd))