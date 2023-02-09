# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
quantity1 = int(input("Enter a quantity of set one: "))
quantity2 = int(input("Enter a quantity of set two: "))
list1 = []
list2 = []
for i in range(quantity1):
    elements1 = random.randint(0, 100)
    list1.append(elements1)
for i in range(quantity2):
    elements2 = random.randint(0, 100)
    list2.append(elements2)
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
list3 = list(set1.intersection(set2))
print(sorted(list3))


