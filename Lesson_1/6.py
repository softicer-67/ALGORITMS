"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

num = int(input('Введите номер буквы от 1 до 26: '))

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Номер', num, 'соответствует букве: ', alphabet[num - 1])
