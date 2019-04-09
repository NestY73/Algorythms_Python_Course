#-------------------------------------------------------------------------------
# Name:        firm_margin
# Purpose:     Homework_lesson_5_Algorythm
#
# Author:      Fujitsu
#
# Created:     10.04.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

firma = {}
n = int(input("Количество предприятий"))
s = 0
for i in range(n):
    fName = input(str(i + 1) + " -ая фирма")
    volume = int(input("Прибыль "))
    firma[fName] = volume
    s += volume

avrg = s / n
print("Средняя прибыль {}".format(avrg))
print('Прибыль данных фирм выше среднего:')
for i in firma:
    if firma[i] > avrg:
        print(i)
print('Прибыль данных фирм ниже среднего:')
for i in firma:
    if firma[i] < avrg:
        print(i)