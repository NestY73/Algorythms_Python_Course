#-------------------------------------------------------------------------------
# Name:        quantity_substring
# Purpose:     Homework_Lesson_8
#
# Author:      Fujitsu
#
# Created:     19.04.2019
# Copyright:   (c) Fujitsu 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

S = str(input("Введите строку S: "))

print("Строка {:s} имеет длину {:d} символов.".format(S, len(S)))

subs_set = set()
for i in range(len(S)):
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))


print("Количество различных подстрок в этой строке:", len(subs_set))