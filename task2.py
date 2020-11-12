# Основы Python
# Урок 1
# Практическое задание 1

# 1

# тут все просто все понятно

# 2
userSecond = int(input('Введите любое количество секунд :'))

minutes = userSecond // 60
hour = minutes // 60
minutes = minutes - (hour * 60)
second = userSecond - (minutes * 60)
print(f'{hour}:{minutes}:{second}')

# 3
user = input('Введите число n: ')
answer = int(user) + int(user + user) + int(user + user + user)
print(f'{user} + {user + user} + {user + user + user} = ' + str(answer))

# 4
usernum = int(input('целое положительное число :'))
usermax = usernum % 10
usernum = usernum // 10
while usernum > 0:
    if usernum % 10 > usermax:
        usermax = usernum % 10
    usernum = usernum // 10
print(usermax)

# 5
userProceeds = int(input('Введите значение выручки Вашей фирмы : '))
userCosts = int(input('Введите значение издержек Вашей фирмы : '))
if userProceeds == userCosts:
    print('Ваша фирма работает в ноль \nНадо сокращать издержки :)')
else:
    if userProceeds > userCosts:
        prof =  userProceeds / userCosts
        print(f'Ваша фирма работает c прибылью \nРетабильность Вашей фирмы {prof:.2f}%')
        userEmployees = int(input('Введите численность сотрудников Вашей фирмы : '))
        profit = (userProceeds - userCosts) / userEmployees
        print(f'Приыль Вашей фирмы в расчете на одного сотрудника составляет: {profit}%')
    else:
        print('Ваша фирма работает в убыток \nРентабельностью тут и не пахнет')

# 6
userОneDay = int(input('Введите результат первого дня тренировки в киллометрах: '))
userKm = int(input('Какого результа Вы хотите добиться в киллометрах: '))
userKm10 =  userОneDay * 0.1

x = 1

while True:
    userОneDay += userKm10
    x += 1
    if userОneDay >= userKm:
        break
    else:
        continue

print (f'на {x}-й день Вы достигните результа - не менее {userKm} км.')
