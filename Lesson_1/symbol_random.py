#-------------------------------------------------------------------------------
# Name:        symbol_random
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#случайный символ
import random

sym1 = input('Введите первую букву диапазона (английские, нижний регистр)')
sym2 = input('Введите вторую букву диапазона (английские, нижний регистр)')

alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sym1_ind = alph.index(sym1)
sym2_ind = alph.index(sym2)

rand_sym = alph[random.randint(sym1_ind, sym2_ind)]

print(f'Случайная буква из выбранного вами дипазона - "{rand_sym}"')

#Пользователь вводит две буквы. Определить, на каких местах алфавита
#они стоят и сколько между ними находится букв.

sym1 = input('Введите первую букву (английские, нижний регистр)')
sym2 = input('Введите вторую букву (английские, нижний регистр)')

sym1_ind = alph.index(sym1)
sym2_ind = alph.index(sym2)

print(f'Выбранные вами буквы имеют порядковые номера: '
        f'{sym1} = {sym1_ind}, {sym2} = {sym2_ind},'
            f' и между ними находятся {sym2_ind - sym1_ind - 1} букв')



#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num_sym = int(input('Введите порядковый номер буквы'))

print(f'Под номеров {num_sym} находится буква "{alph[num_sym]}"')
