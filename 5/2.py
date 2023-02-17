# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random
list = []
n = int(input("Enter a quantity of marks: "))

def fill_list (n):
    for i in range(n):
        mark = random.randint(1, 5)
        list.append(mark)
    return list

print(fill_list(n)) 
for i in range(len(list)):
    if list[i] == 5 or list[i] == 4:
        list[i] = 1
print(list)

  
            
        
