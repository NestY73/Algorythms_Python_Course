#-------------------------------------------------------------------------------
# Name:       calc_simple
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     26.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Для завершения работы программы введите ноль(0) в качестве знака\
 операции ")
while True:
        s = input("Введите знак операции (+,-,*,/): ")
        if s == '0': break
        if s in ('+','-','*','/'):
                x = float(input("x="))
                y = float(input("y="))
                if s == '+':
                        print("Результат сложения {:.2f} и {:.2f} равен: {:.2f}".format(x,y,x+y))
                elif s == '-':
                        print("Результат вычитания из {:.2f} числа {:.2f} равен: {:.2f}".format(x,y,x-y))
                elif s == '*':
                        print("Результат умножения {:.2f} на {:.2f} равен: {:.2f}".format(x,y,x*y))
                elif s == '/':
                        if y != 0:
                                print("Результат деления {:.2f} на {:.2f} равен: {:.2f}".format(x,y,x/y))
                        else:
                                print("Деление на ноль!")
        else:
                print("Неверный знак операции!")