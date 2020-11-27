# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:00:44 2020

@author: slimexpert
"""
#1
try:
    with open('task1.txt','w') as file_object:
        while True:
            user_text = input('Введите строку: ')
            if user_text != ' ':
                file_object.writelines(user_text + '\n')
            else:
                print('Файл сохранен: \n')
                file_object.close()
                file_object = open('task1.txt','r', encoding='UTF-8')
                file_cont = file_object.read()
                print('Вот что у Вас получилось:\n' + file_cont)
                break
except IOError:
    print('Произошла ошибка открытия файла')
finally:
    file_object.close()
   
#2
try:
    with open('task6_2.txt','r', encoding='UTF-8') as file_object: 
        x = 0
        for el, i in enumerate(file_object):
            print(f'в строкe {el + 1} - {len(i.split())} слов')
            x += 1
        print(f'В файле {x} строк(и)')
except IOError:
    print('Произошла ошибка открытия файла')
finally:
    file_object.close()
   
#3
#task6_3.txt
#Иванов С.А. 15800
#Филатов Д.А. 25960
#Шишкин С.Ю. 18523
#Васильева Т.И. 20050
#Сапункова И.П. 29850
#Дмитриев И.П. 19600

try:
    with open('task6_3.txt','r', encoding='UTF-8') as file_object: 
        list_read = [el.split() for el in file_object]
        list_zp20 = []
        employees_count=0
        average_zp = 0
        for i in list_read:        
            if int(i[2]) > 20000:
                list_zp20.append(i[0])
            employees_count += 1
            average_zp += int(i[2])
        print(f'Список сотрудников с зп большей 20 т.р. - {list_zp20}')
        print(f'Кол-во сотрудников - {employees_count}')
        print(f'Средняя величина дохода - {average_zp / employees_count}')
except IOError:
    print('Произошла ошибка открытия файла')
finally:
    file_object.close()

#4
list_number = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
list_read = {}
try:
    with open('task6_4.txt','r', encoding='UTF-8') as file_one:
        for i in file_one:
            list_read[list_number[i.split('-')[0].rstrip()]] = i.split('-')[1]
    with open('task6_4_1.txt','w') as file_two:
        for key, value in list_read.items():
            file_two.write(str(key) +' - '+ str(value))
except IOError:
    print('Произошла ошибка чтения или записи файла')
finally:
    file_one.close()
 
#5 Выход из бесконечно цикла не стал делать и так опаздываю за лекциями из за работы
user_summ = 0
try:
    with open('task6_5.txt', 'w') as file_object:
        while True:
            user_numb = int(input('Введите любое число: '))
            file_object.write(str(user_numb) + ' ')
            print(f'Число {user_numb} записано в файл')
            user_summ += user_numb
            print (f'Сумма введенных чисел {user_summ}')       
except IOError:
    print('Произошла ошибка чтения или записи файла')
finally:
    file_object.close()

#6 
def numb_str(user_str):
    result = ''.join(el if el in '0123456789' else ' ' for el in user_str)
    return [int(el) for el in result.split()]
user_dict = {}
try:
    with open('task6_6.txt', 'r', encoding='UTF-8') as file_object:
        for i in file_object:
            srez = i[:i.index(':')]
            user_dict[srez] = sum(numb_str(i))
        print(user_dict)
except IOError:
    print('Произошла ошибка чтения или записи файла')
finally:
    file_object.close()

#7
#task6_7.txt
#firm_1 ООО 10000 5000
#firm_2 ООО 10000 15000
#firm_3 ООО 20000 7000
#firm_4 ООО 10000 11000
#firm_5 ООО 30000 9000

import json
firm_profit = {}
firm_avange_profit = {}
firm_damages = {}
summ = 0
try:
    with open('task6_7.txt', 'r', encoding='UTF-8') as file_object:
        for i in file_object:
            firm_line = i.split()
            firm_profit[firm_line[0]] = int(firm_line[2])
            summ += int(firm_line[2])
            if int(firm_line[2]) < int(firm_line[3]):
                firm_damages[firm_line[0]] =  int(firm_line[2]) -  int(firm_line[3]) 
        firm_avange_profit['average_profit'] = summ
        list_json = [firm_profit, firm_avange_profit,firm_damages ]
        with open('task6_7.json', 'w', encoding='UTF-8') as file_json:
            json.dump(list_json, file_json)
except IOError:
    print('Произошла ошибка чтения или записи файла')
finally:
    file_object.close()
















