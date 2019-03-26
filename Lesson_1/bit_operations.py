#-------------------------------------------------------------------------------
# Name:        bit_operations
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n1 = int(input("Введите первое число: "))
n2 = int(input("Введите второе число: "))

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print("Результат побитового OR: %10s" % bin(bit_or))
print("Результат побитового AND: %10s" % bin(bit_and))
print("Результат побитового XOR: %10s" % bin(bit_xor))
print("Результат побитового сдвига на 2 разряда вправо: %10s" %bin(n1>>2))
print("Результат побитового сдвига на 2 разряда  влево: %10s" %bin(n1<<2))
