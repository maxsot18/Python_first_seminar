# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


input_text = list(input("Enter a text: "))
count = 0
list = set(input_text)
for item in list:
    for item1 in input_text:
        if item1 == item:
            count += 1
            print(f"{item1}_{count}")
    count = 0       


