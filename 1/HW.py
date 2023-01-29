# ; Задача 1: Найдите сумму цифр трехзначного числа.
# ; 123 -> 6 (1 + 2 + 3)
# ; 100 -> 1 (1 + 0 + 0)

input = int(input("Enter a number: "))
sum = 0
while input > 0:
    sum = sum + input % 10
    input = input // 10
    
print(f"Sum of numbers = {sum}")

      
