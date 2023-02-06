# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
import random

# k = int(input("Enter a value"))
# list = []
# for i in range(5):
#     value = random.randint(0, 10)
#     list.append(value)
# print(list)
# for i in range(k):
#     list.insert(0, list.pop())
# print(list)
list = [1, 2, 3, 4, 5]
result_list = []
k = int(input("Enter :"))
k = - (k % len(list))
for i in range(len(list)):
    result_list.append(list[k])
    k = k + 1
print(result_list) 
print(k)   

    

        
