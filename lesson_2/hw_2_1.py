'''
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''

line = [1, 2, 4.23, True, False, "string", -3]
print("Список имеет тип: ", type(line))
index = 1
for varIndex in line:
    print(f'Элемент {index} имеет тип: {type(varIndex)}')
    index += 1
