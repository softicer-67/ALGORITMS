'''
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
'''


def menu():
    print('[+] Сложение\n'
          '[-] Вычитание\n'
          '[*] Умножение\n'
          '[/] Деление\n'
          '[0] Выход')


menu()
option = input()

while option != '0':
    if option == '+':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} + {b} =', a + b)
    elif option == '-':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} - {b} =', a - b)
    elif option == '*':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        print(f'{a} * {b} =', a * b)
    elif option == '/':
        try:
            a = int(input('Введите первое число:'))
            b = int(input('Введите второе число:'))
            print(f'{a} / {b} =', round(a / b, 4))
        except ZeroDivisionError:
            print('Ошибка! На <0> делить нельзя!')
    else:
        print('Ошибка, введите правильный  символ:')
    menu()
    option = input()
