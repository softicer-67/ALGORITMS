'''
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
'''


import random

print('\nИгра угадай число от 0 до 100 за 10 попыток.\n')


def menu():
    print('[Y] - Играть ')
    print('[N] - Выйти ')


menu()
option = input()
rnd = random.randint(0, 100)
count = 0

while option != 'N':
    while count != 10:
        my = int(input('Введи число : '))
        if my < rnd:
            print(f'Загаданное число больше {my}')
        elif my > rnd:
            print(f'Загаданное число меньше {my}')
        else:
            print(f'\nВы угадали число "{rnd}" за {count + 1} попыток\n')
            menu()
            option = input()
            count = -1
            if option == 'N':
                break
            rnd = random.randint(0, 100)
        count += 1
    else:
        print(f'Вы не угадали число за {count} попыток... Загаданное число "{rnd}"\n')
        menu()
        option = input()
        count = 0
        if option == 'N':
            break
        rnd = random.randint(0, 100)
