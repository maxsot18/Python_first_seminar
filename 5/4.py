# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def reverse(n: int):
    if n == 0:
        return ""
    num = input("Enter numbers: ")
    return reverse (n - 1) + num
quantity = int(input("enter a quantity: "))
print(reverse(quantity))