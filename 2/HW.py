#  На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
# import random
# n = int(input("Enter a quantity of coins : "))

# sides = []
# count1 = 0
# count0 = 0
# for i in range(n):
#     sides.append(random.randint(0,1))
#     if sides[i] == 0:
#         count1 += 1
#     else:
#         count0 += 1
# print(sides)        
# if count1 > count0 or count1 == count0:
#     print(count0)
# else:
#     print(count1)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# import random

# num1 = random.randint(1,10)
# num2 = random.randint(1,10)

# print(f"Sum of numbers is = {num1 + num2}")
# print(f"Product of numbers is =  {num1 * num2}")
# answer = int(input("Enter a number one : "))
# answer1 = int(input("Enter a number two : "))

# if (answer == num1 or answer == num2) and (answer1 == num1 or answer1 == num2):
#     print(f"Yes, you a right! The numbers are {num1} and {num2}")
# else:
#     print(f"No, you are stupid!! The numbers are {num1} and {num2}")

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

input_number = int(input("Enter a number : "))
square = 1
while square < input_number:
    print(square)
    square *= 2
    
    
 
    



   
        










            
        
    
    



   