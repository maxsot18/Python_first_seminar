# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random

list = []

for i in range(8):
    value = random.randint(0, 10)
    list.append(value)
print(list)
print(len(set(list)))    