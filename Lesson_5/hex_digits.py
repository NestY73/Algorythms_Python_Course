#-------------------------------------------------------------------------------
# Name:        hex_digits
# Purpose:     Homework_Lesson_5_Algorythms
#
# Author:      Fujitsu
#
# Created:     10.04.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

hex1 = list(input("Введите первое число"))
hex2 = list(input("Введите второе число"))

sum = hex(int(''.join(hex1), 16) + int(''.join(hex2), 16)).split('0x')[1]
multiply = hex(int(''.join(hex1), 16) * int(''.join(hex2), 16)).split('0x')[1]

print(sum, multiply)