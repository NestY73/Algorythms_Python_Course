#-------------------------------------------------------------------------------
# Name:        ascii_symbols
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     26.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for i in range(32,128):
    print("{:4d}-{:s}".format(i,chr(i)), end ='')
    if i % 10 == 0:
        print()

print()