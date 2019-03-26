#-------------------------------------------------------------------------------
# Name:        random_function
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

start = int(input("Введите начальное число диапазона:"))
finish = int(input("Введите финальное число диапазона:"))
choice = 'y'

while choice == 'y':
    n = random.randint(start,finish)
    r = random.uniform(start,finish)
    print("Случайное целое число:",n)
    print("Случайное вещественное число:{0:.2f}".format(r))
    choice = input("Хотите еще генерацию (y/n)?")