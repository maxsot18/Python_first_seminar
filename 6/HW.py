# Задача 30: Заполните массив элементами арифметической прогрессии. Её 
# первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def fill_list (n):
#     list = []
#     step = int(input("enter a step: "))
#     first_elem = int(input("enter a first el:"))
#     for i in range(quan):
#         list.append(first_elem)
#         first_elem += step
#     return list

# quan = int(input("enter a quantity of elements: ")) 
# print(fill_list(quan))        

# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def fill_array (n):
    list = []
    for i in range(n):
        value = random.randint(1, 10)
        list.append(value)
    print(list)
    i1 = int(input("Enter a start: "))
    i2 = int(input("Enter the end: "))
    list_1 = list[i1 - 1:i2]
    print(list_1)
    
    for i in range(len(list_1)):
        print(i + i1)

n = random.randint(8,15)
fill_array(n)


    