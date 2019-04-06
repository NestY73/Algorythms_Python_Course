#-------------------------------------------------------------------------------
# Name:        find_simple
# Purpose:
#
# Author:      Fujitsu
#
# Created:     06.04.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import sqrt

def foo():
    list = set()
    for i in range(300):
        for j in range(2, 1 + int(sqrt(i))):
            if not i % j:
                break
        else:
            list.add(i)
    print(list)

foo()