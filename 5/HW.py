# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# def power_of_a(a, b):
#     if b == 2:
#         return a * a
#     if b == 1:
#         return a
#     return power_of_a(a, b - 1) * a

# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))

# print(f"The power of number {a} = {power_of_a(a, b)}")

# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4



def sum(a, b):
    if a == 1:
        return a + b
    return sum(a - 1, b + 1)

a = int(input("Enter a first number: "))
b = int(input("enter a second number: "))
print(f"Sum of two numbers = {sum(a, b)}")
