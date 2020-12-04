# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:20:44 2020

@author: slimexpert

"""
#1
class Matrix:
    def __init__(self, *args):
        self.matrix_list = []
        for el in args:
            self.matrix_list.append(el)
    def __str__(self):
        str_matr = ''
        for el in self.matrix_list:         
            for x in el:
                str_matr = str_matr + ' ' + str(x)
            str_matr = str_matr + '\n'
        return str_matr
    def __add__(self, matrix2):
        sum_matrix_list = []
        for i, el in enumerate(self.matrix_list):
            sum_matrix_list.append([x+y for x,y in zip(self.matrix_list[i], matrix2.matrix_list[i])])
        return Matrix(sum_matrix_list)

matrix_obj1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix_obj1)

matrix_obj2 = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
print(matrix_obj2)

print(matrix_obj1 + matrix_obj2)

#2

from abc import ABC, abstractmethod

class dress(ABC):
    def __init__(self, title):
        self.title = title
    
    @abstractmethod
    def fabric_consumption(self):
        pass
   
    def __add__(self, dress):
        return self.fabric_consumption + dress.fabric_consumption
       
class coat(dress):
    def __init__(self,title, size):
        super().__init__(title)
        self.size = size
    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)
        
class costume(dress):
    def __init__(self, title, growth):
        super().__init__(title)
        self.growth = growth
    @property
    def fabric_consumption(self):
        return round(2 * self.growth + 0.3, 2)
        

coat_obj = coat('Пальто', 56)
print(coat_obj.fabric_consumption)
costume_obj = costume('Костюм', 181)
print(costume_obj.fabric_consumption)

print(costume_obj + coat_obj)


#3
class organic_cell:
    def __init__(self, cell_count): 
        self.cell_count = cell_count
        
    def __add__(self, cell):
        return organic_cell(self.cell_count + cell.cell_count)
    
    def __sub__(self, cell):
        if (self.cell_count - cell.cell_count) > 0:
           return organic_cell(self.cell_count - cell.cell_count)
        else:
           return 'Вычитание исходных клеток не возможно.'
       
    def __mul__(self, cell):
        return organic_cell(self.cell_count * cell.cell_count)
    
    def __floordiv__(self, cell):
        return organic_cell(self.cell_count // cell.cell_count)
    
    def __str__(self):
        return f'число ячеек в клетке - {self.cell_count}'
    # Скопировал и разбора домашки, сам так и не додумался как это сделать
    # Пребирал строки и ни чего не получалось (    
    def make_order(self, row_count):
        return '\n'.join(['*' * row_count for _ in range(self.cell_count // row_count)]) + '\n' + '*' *(self.cell_count % row_count)
        


cell_obj = organic_cell(18)
cell_obj1 = organic_cell(4)
print(cell_obj)
print(cell_obj1)

print(f'Сложение 2-х исходных клеток: {cell_obj + cell_obj1}')
print(f'Вычитание 2-х исходных клеток: {cell_obj - cell_obj1}')
print(f'Умножение 2-х исходных клеток: {cell_obj * cell_obj1}')
print(f'Деление 2-х исходных клеток: {cell_obj // cell_obj1}')
print(f'Вывод по рядам \n{cell_obj.make_order(5)} ')


