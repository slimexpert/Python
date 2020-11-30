# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:14:05 2020

@author: slimexpert
"""

#1
import time
class TrafficLight:
    __color = {1:'Красный', 2:'Желтый', 3:'Зеленый'}
    
    def running(self):
        for key, value in self.__color.items():
            if value == 'Красный':
                print(value)
                time.sleep(7)
            else:
                if value == 'Желтый':
                    print(value)
                    time.sleep(2)   
                else:
                    print(value)
                    time.sleep(3)   

obj = TrafficLight()
obj.running()

#2
class Road:
    __massa1m_kg = 25
    
    def __init__(self, length, width):
        self._length = length
        self._width  = width
    
    def call(self, thickness):
        print(f'{(self._length * self._width * self.__massa1m_kg * thickness) / 1000} т.')

obj = Road(20, 5000)
obj.call(5)

#3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
    
class Position(Worker):
    def get_full_name(self):
        return f'Ваше имя: {self.surname} {self.name}'
    def get_total_income(self):
        return f'Ваш доход: {self._income["wage"] + self._income["bonus"]} руб.'
       

obj = Position('Сергей', 'Никитин', 'Генеральный директор', {'wage': 150000, 'bonus': 35000})
print(obj.get_full_name())
print(obj.get_total_income())

#4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return f'{self.color} {self.name} - поехала со скоростью {self.speed} км/час'
    def stop(self):
        return f'{self.color} {self.name} - остановилась'
    def turn(self, direction):
        return f'{self.color} {self.name} - поворачивает на {direction}'
    def show_speed(self):
        return f'Текущая скорость {self.color} {self.name} - {self.speed} км/час'
    def turn_on_flasher(self, turn):
        if self.is_police == True:
            return print('Мигалка включена') if turn else print('Мигалка выключена')
        else:
            return f'Это не полицейская машина. Это {self.color} {self.name}'
        
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Осторожно {self.color} {self.name} ваша скорость выше 60 км/час'
        else:
            return f'Текущая скорость {self.color} {self.name} - {self.speed} км/час'

class SportCar(Car): 
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Осторожно {self.color} {self.name} ваша скорость выше 40 км/час'
        else:
            return f'Текущая скорость {self.color} {self.name} - {self.speed} км/час'
      
class PoliceCar(Car): 
    pass

print ('x' * 50)
obj_car_towr = TownCar(80, 'Коричневый', 'Volvo', False)
print(obj_car_towr.go())
print(obj_car_towr.show_speed())
print(obj_car_towr.turn_on_flasher(True))
print(obj_car_towr.turn('право'))
print(obj_car_towr.stop())
print ('x' * 50)
obj_car_police = PoliceCar(100, 'Белый', 'ВАЗ 2112', True)
print(obj_car_police.go())
print(obj_car_police.show_speed())
print(obj_car_police.turn_on_flasher(True))
print(obj_car_police.turn('Лево'))
print(obj_car_police.stop())
print ('x' * 50)

#5
class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self, color):
        return f'Запуск отрисовки {self.title}(ой) цвет - {color}'

class Pencil(Stationery):
    def draw(self, marker):
        return f'Запуск отрисовки - {marker} {self.title}'

class Handle(Stationery):
    def draw(self, width):
        return f'Запуск отрисовки - {self.title} ширина {width} мм.'
    
obj = Pen('Ручка')
print(obj.draw('Красный'))

obj = Pencil('Карандаш')
print(obj.draw('твёрдо-мягкий'))

obj = Handle('Маркер')
print(obj.draw(50))



            

    

























        