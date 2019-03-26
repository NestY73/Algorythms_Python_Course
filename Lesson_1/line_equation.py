#-------------------------------------------------------------------------------
# Name:        line_equation
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Координаты точки A(x1; y1):")
x1 = float(input("x1 = "))
print("x1 =", x1)
y1 = float(input("y1 = "))
print("y1 =", y1)

print("Координаты точки B(x2; y2):")
x2 = float(input("x2 = "))
print("x2 =", x2)
y2 = float(input("y2 = "))
print("y2 =", y2)

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))
