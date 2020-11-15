# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:40:16 2020

@author: slimexpert
"""

# Основы Python 
# Урок 2
# Практическое задание 1

# 1 

free_list = ['строка', 4, 3.5, False, 'Втора строка', (1,2,3), [4,5,6]]
for i in free_list:
    print(type(i))

# 2

count = int(input('Из какого кол-ва элементов вы хотите получить список: '))
i = 0
user_list = []
while i <= count - 1:
    user_list.append(input('Заполните список значениями: '))
    i += 1

result_list = []
if len(user_list) % 2 == 0:
    n=0
    for n in range(len(user_list)-1):
        if n % 2 == 0:
            result_list.append(user_list[n+1])
            result_list.append(user_list[n])     
    print ('*' * 100)
    print (f'Вот ваш перевернутый список: {result_list}')    
    print ('*' * 100)   
else:
    print ('*' * 100)
    print (f'Кол-во элементов нечетное, список остался без изменений: {user_list}')    
    print ('*' * 100)
    
# 3

user_mont = int(input('Видите номер месяца от 1 до 12: '))
mont_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
if user_mont <= 12: 
    print ('*' * 50)
    print(f'Это - {mont_list[user_mont + 1]} (решение простым списком)') 
else: 
    print('Такого месяца не бывает')
print ('*' * 50)

mont_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
if user_mont <= 12: 
    print ('*' * 50)
    print(f'Это - {mont_dict[user_mont]} (решение со словарем)') 
else: 
    print('Такого месяца не бывает')
print ('*' * 50)


# 4
user_text = input('Видите строку из нескольких слов, разделённых пробелами: ')

text = user_text.split(' ')
x = 1
for element in text:
    if len(element) >= 10:
        s = element[0:10:1] + '...'
    else:
        s = element
    print(f'{x} - {s}')
    x +=1


# 5
rate_list = [7, 5, 3, 3, 2]
x = 1
count = 5
while count >= x :
    rate_list.append(int(input('Введи новый елемент рейтинга, у Вас ' +str(count)+ ' попыток(и): ')))
    rate_list.sort(reverse=True)
    print(f'Ваш новый рейтинг - {rate_list}')
    count -= 1
    

# 6

text_name = 'Наименование'
text_summ = 'Цена'
text_kol = 'Кол-во'

count_pos = int(input('Сколько товаров Вы хотите добавить: '))
number_pos = 1
product_list =[]
while number_pos <= count_pos:
    product_name = input('Введите наименование '+ str(number_pos) + '-го товара: ')
    product_summ = int(input('Введите стомость '+ str(number_pos) + '-го товара: '))
    product_kol = int(input('Введите кол-во '+ str(number_pos) + '-го товара: '))
    
    product_list.append((number_pos, {text_name:product_name, text_summ: product_summ, text_kol: product_kol,},))
    number_pos += 1

list_name = []
list_summ = []
list_kol = []
for element in product_list:
    list_name.append(element[1].get(text_name))
    list_summ.append(element[1].get(text_summ))
    list_kol.append(element[1].get(text_kol))
product_analitic = {text_name: list_name, text_summ:list_summ, text_kol: list_kol }

print ('*' * 100)
print(product_analitic)
print ('*' * 100)







    
