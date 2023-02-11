# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# import random
# quantity1 = int(input("Enter a quantity of set one: "))
# quantity2 = int(input("Enter a quantity of set two: "))
# list1 = []
# list2 = []
# for i in range(quantity1):
#     elements1 = random.randint(0, 100)
#     list1.append(elements1)
# for i in range(quantity2):
#     elements2 = random.randint(0, 100)
#     list2.append(elements2)
# set1 = set(list1)
# set2 = set(list2)
# print(set1)
# print(set2)
# list3 = list(set1.intersection(set2))
# print(sorted(list3))

# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9
import random
input_value = int(input("Enter a quantity of bushs: "))
quantity_of_bushes = [i + 1 for i in range(input_value)]
print(f"Bushs on the field : {quantity_of_bushes}") 

bush = quantity_of_bushes[random.randint(1, input_value - 2)]
print(f"Selected bush : {bush}")
bushes1 = quantity_of_bushes[bush - 2: bush + 1]
a = random.randint(1,5)
print(f"Selected bushes : {bushes1}")
berries = 1
for item in bushes1:
    berries += a
print(f"Quantity of berries from selected bushes = {berries}")
    
    
    
    


    
       
    
    

