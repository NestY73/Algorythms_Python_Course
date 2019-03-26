#-------------------------------------------------------------------------------
# Name:        max_sum_digits
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     26.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input("Введите число (0 - окончание ввода)"))
max_sum = 0
max_num = 0
while n != 0:
    num = n
    s = 0
    while n>0:
        s += n % 10
        n //= 10
    print("Число {:>10d} имеет сумму цифр: {:>5d}".format(num,s))
    if s > max_sum:
        max_sum = s
        max_num = num
    n = int(input("Введите число (0 - окончание ввода)"))
print('Число {:d} имеет максимальную сумму цифр: {:d}'.format(max_num, max_sum))
