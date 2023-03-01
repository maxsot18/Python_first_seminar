# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

data_path = 'filenew.txt'
def append_contact():
    contact = input("Введите данные: ")
    with open (data_path, 'a') as f:
       f.write(f'\n{contact}')
        
def read_file(data_path):
    with open (data_path, 'r') as f:
        print(f.read())

def search_line(data_path):
    search_by = input("Введите данные для поиска: ")
    with open (data_path, 'r') as f:
        for line in f:
            if search_by in line:
                print(line)
def change_data(data_path):
    search_data = input("Введите данные которые нужно заменить: ")
    change_data = input("введите новые данные: ")
    with open(data_path, "a") as f:
        for line in f:
            if search_data in line:
                line.replace(search_data, change_data)
                line.write(change_data)
                    

def user_action():
    print("Добрый день! Какие действи вы хотите произвести со справочником? Выберите один из вариантов ниже: \n 1: Вывести весь справочник \n 2: Найти информацию \n 3: Добавить информацию в справочник")
    input1 = int(input("Выберите вариант для работы со справочником: "))
    if input1 == 1:
        read_file(data_path)
    elif input1 == 2:
        search_line(data_path)
    elif input1 == 3:
        append_contact()
        print('Контакт добавлен')
    elif input1 == 4:
        change_data(data_path)
    else:
        print('Такого варианта нет!')
user_action()
        