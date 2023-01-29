# ; Задача 1: Найдите сумму цифр трехзначного числа.
# ; 123 -> 6 (1 + 2 + 3)
# ; 100 -> 1 (1 + 0 + 0)

# input = int(input("Enter a number: "))
# sum = 0
# while input > 0:
#     sum = sum + input % 10
#     input = input // 10
    
# print(f"Sum of numbers = {sum}")

# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

full_quantity = int(input("Enter a full quantity: "))
if full_quantity % 3 == 0 and full_quantity % 2 == 0:
    print (f"Peter made {int(full_quantity / 3 / 2)}")
    print (f"Sergey made {int(full_quantity / 3 / 2)}")
    print (f"Kate made {int(full_quantity / 3 * 2)}")
else:
    print ("Enter an another number")
    


      
