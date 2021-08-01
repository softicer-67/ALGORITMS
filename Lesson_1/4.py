"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random


def menu():
    print('\n\tМЕНЮ:\n\n\
    [1] Вывести случайное целое число\n\
    [2] Случайное вещественное число\n\
    [3] Случайный символ\n\
    [0] Выход')


def num_choice():
    print('Задайте границы диапазона: ')
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    if a > b:
        return random.randint(b, a)
    return random.randint(a, b)


def alpha_choice():
    print('Задайте границы диапазона: ')
    c = input('Первая буква: ')
    d = input('Вторая буква: ')
    if c == '' or d == '' or c.isdigit() or d.isdigit():
        res = '\nОшибка ввода!\n'
    elif ord(c) < ord(d):
        res = random.choice([chr(i) for i in range(ord(c), ord(d) + 1)])
    else:
        res = random.choice([chr(i) for i in range(ord(d), ord(c) + 1)])
    return res


menu()
option = input()

while option != '0':
    if option == '1':
        try:
            print(num_choice())
        except ValueError:
            print('\nОшибка ввода!\n')
    elif option == '2':
        try:
            print(float(num_choice()))
        except ValueError:
            print('\nОшибка ввода!\n')
    elif option == '3':
        print(alpha_choice())

    print('Меню: [1], [2], [3] или [0]')

    if __name__ == '__main__':
        option = input()
