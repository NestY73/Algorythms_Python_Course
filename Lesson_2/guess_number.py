#-------------------------------------------------------------------------------
# Name:        guess_number
# Purpose:     Homework_lesson2_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#
# Author:      Fujitsu
#
# Created:     16.03.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import random
num = round(random() * 100)
count = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while count <= 10:
    att = int(input(str(count) + '-я попытка: '))
    if att > num:
        print('Много')
    elif att < num:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % count)
        break
    count += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', num)