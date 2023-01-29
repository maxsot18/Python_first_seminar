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

# full_quantity = int(input("Enter a full quantity: "))
# if full_quantity % 3 == 0 and full_quantity % 2 == 0:
#     print (f"Peter made {int(full_quantity / 3 / 2)}")
#     print (f"Sergey made {int(full_quantity / 3 / 2)}")
#     print (f"Kate made {int(full_quantity / 3 * 2)}")
# else:
#     print ("Enter an another number")

# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером.
# Cчастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# input = int(input("Enter a number of ticket "))
# sum = 0
# sum1 = 0 
# ticket =input // 1000
# ticket1 =input % 1000
# if input > 100000 and input < 1000000:
#     while ticket % 10 > 0:
#         sum =  sum + ticket % 10
#         sum1 = sum1 + ticket1 % 10
#         ticket //= 10
#         ticket1 //= 10
# else:
#     print("Enter a six digit number")

# if sum == sum1:
#     print("Yes")
# else:
#     print('No')  

# Задача 4: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input("Enter a first value: "))
m = int(input("Enter a second value: "))
k = int(input("Enter a quantity of pieces: "))
if k % m == 0 or k % n == 0:
    print("Yes")
else:
    print("No")              
     
           
    


      
