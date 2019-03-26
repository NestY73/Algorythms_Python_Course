#-------------------------------------------------------------------------------
# Name:        visokos_year
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')