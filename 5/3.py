# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input("Enter a number: "))

def simple_number (n):
    if (n % 1 == 0 and n % n == 0):
        return True
print(simple_number(n))