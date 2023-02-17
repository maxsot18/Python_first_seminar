# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return Fibonacci(n - 2) + Fibonacci(n - 1)

n = int(input("Enter a value: "))

print(Fibonacci(n))

        
    
    
        
  
        
    
        
    
    


