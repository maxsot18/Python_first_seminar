# Требуется вычислить, сколько раз встречается некоторое число X в 
# массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1
import random
array = []
n = int(input("Enter a length of array:"))
count = 0
x = random.randint(0, 10)
print(f"The number to find is : {x}")
for i in range(n):
    value = random.randint(0, 10)
    array.append(value)
print(array)  

for i in range(len(array)):
    if array[i] == x:
        count += 1
           
print(count)         

