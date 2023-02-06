# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
import random
list = []

for i in range(8):
    value = random.randint(1,10)
    list.append(value)
print(list)
count = 0
i = 1
for i in range(len(list) - 1):
    if list[i] < list[i + 1]:
        count += 1
    else:
        continue
    i += 1    
print(count)            