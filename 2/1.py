# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

input = int(input("Enter a number: "))
number = 1
factorial = 1
if input >= 0:
    while number <= input:
        factorial *= number 
        number += 1
    print(f"Factorial of number {input} = {factorial}" )
else:
    print("Enter a positive number ")       