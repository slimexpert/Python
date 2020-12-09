# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:14:19 2020

@author: slimexpert

"""
#1
 
#параметры запуска скрипта [Фамилия, выработка в часах, пермия за месяц] 
#ставка за час как правило фиксированая величина и равняется 207 р/час

from sys import argv # скрипт zp.py 10 Иванов 167 3000

user_param = ['Иванов', '167', '3000']

#name, per_hour, prize = argv 
# переопределяем для работы программы
name, per_hour, prize = user_param

itog = (float(per_hour) * 207) + float(prize)
print(f'{name} заработал {itog} руб.')


#2
# не догнал, как? пока не посмотрел разбор ДЗ, ни когда не встречался с генераторами 
# я пытался через enumerate но постоянно вываливался за границы списка
#после разбора конечно же получилось )
user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [user_list[i] for i in range(1, len(user_list)) if user_list[i-1] < user_list[i]]
print(new_list)


#3 
new_list = [el for el in range(20,240,1) if (el % 20 == 0) or (el % 21 == 0)]
print(new_list)


#4
user_list =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in user_list if user_list.count(el) == 1]
print(new_list)


#5
from functools import reduce 
new_list = [el for el in range(100,1000,1) if el % 2 == 0]
print(reduce(lambda x, y: x*y, new_list))


#6 / 1  
from itertools import count
for i in count(3):
    if i > 10:
        break
    else:
        print(i)

#6 / 2
from itertools import cycle
x = 3
for y in cycle("ABC"):
    if x > 10:
        break
    print(y)
    x += 1

   
#7
def fact(n):
    x = 1
    for i in range(2, n+1):
        x *= i
        yield x
for el in fact(5):
    print(el)
