# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:52:20 2020

@author: slimexpert
"""

#1
def divisionby(a, b):
    if a.isdigit() and b.isdigit() and int(b) != 0:
        return int(a) / int(b)
    return 'На ноль делить нельзя'

print (divisionby(input('Введите делимое: '), input('Введите делитель: ') ))
 

#2
def print_user(name, subname, date_br, city, e_mail, tell):
    return print(f'Вас зовут: {name} {subname}, вы {date_br} года рождения. Вы проживаете в г. {city}, ваш E-mail - {e_mail} и номер телефона {tell}')

user01 = ('Сергей','Никитин','1979','Всеволосжк','slimexpert@gmail.com','+79219529981')

print_user(user01[0], user01[1], user01[2], user01[3], user01[4], user01[4])


#3
def my_func(var_01, var_02, var_03):
    var = [var_01, var_02, var_03]
    var_max_01 = max(var)
    var.remove(var_max_01)
    varm_max_02 = max(var) 
    return var_max_01 + varm_max_02

var_user = [9, 12, 5]

print(f'Исходные данные: {var_user}')
print(f'Сумма наибольших элементов аргументов: {my_func(var_user[0], var_user[1], var_user[2])}')


#4 / 1

def number_raise (x, y):
    y = int(abs(y))
    a = 1
    result = 1
    while a <= y:
        result = result * int(x)
        a += 1
    return 1 / result 

print(number_raise(input('Введите число: '), input('Введите отрицательное число степени: ')))

#4 / 2
otvet = lambda x, y: 1 / (int(x) ** int(y[1:]))
print(otvet(input('Введите число: '), y = input('Введите отрицательное число степени: ')))

#5

sum_user = 0
while True:
    user_list = input('Ведите числа разделенные пробелом: ').split(' ')
    number_list = list(filter(str.isdigit, user_list))
    if len(number_list) == len (user_list):
        number_list = list(map(int, number_list))
        sum_user += sum(number_list)
        print(f'Сумма введенных чисел: {sum_user}')
    else:
        number_list = list(map(int, number_list))
        sum_user += sum(number_list)
        print(f'Сумма введенных чисел: {sum_user} \nБаста карапузики, игра закончена')
        break


#6

def int_func(str_title):
    return str_title.title()
print(int_func(input('Ведите слова в нижнем регистре: ')))

str_title = lambda user_str: user_str.title()
print(str_title(input('Ведите слова в нижнем регистре: ')))

#6 / 1

def int_func(str_title):
    return str_title.title()

str_title = lambda user_str: user_str.title()

user_text = input('Ведите слова в нижнем регистре разделенные пробелом: ').split(' ')
result_text1, result_text = '' , ''
for x in user_text:
    result_text = result_text + ' ' + int_func(x) 
    result_text1 = result_text1 + ' ' + str_title(x) 
    
print(f'результат 1: {result_text} \nрезультат 2: {result_text1}')
