# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

first_class = int(input("Enter a quantity of pupils of first class : "))
second_class = int(input("Enter a quantity of pupils of second class : "))
third_class = int(input("Enter a quantity of pupils of third class : "))
tables = int(first_class + second_class + third_class + 1) // 2
print(f"Minimal quantity of tables = {tables}")