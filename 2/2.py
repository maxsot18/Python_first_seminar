# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6  

input = int(input("Enter a number : "))
fib = 1
fib1 = 1
index = 0
if input > 1:
    while fib <= input:
        fib2 = fib1
        fib1 = fib
        fib += fib2
        index += 1
    if fib1 == input:
            print(index + 1)
    else:
            print("-1")    
else:
    print("No")

            
           
        
