'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''

from colorama import Fore, Style

company = {}
n = int(input('Колличество предприятий: '))
q = 4  # кварталы
p = 0  # прибыль каждого предприятия
all = 0  # общая прибыль
for i in range(n):
    c_name = input(str(i + 1) + '-е предприятие: ')
    company[c_name] = i + 1
    for j in range(q):
        profit = input('\t' + str(j + 1) + '-ый квартал: ')
        all += int(profit)
        p += int(profit)
    company[c_name] = p
    p = 0
print('Предприятия:', company)
print('Общая прибыль:', all)

avrg = all / n
print('\nСредняя прибыль за год для всех предприятий: %.0f' % avrg)
little = []
big = []
for i in range(n):
    x = int(list(company.values())[i])
    if x > avrg:
        big.append(list(company.items())[i])
    else:
        little.append(list(company.items())[i])

print(f'\nПредприятия с прибылью ВЫШЕ средней: {Fore.GREEN}{big}{Style.RESET_ALL}')
print('=' * 50)
print(f'\nПредприятия с прибылью НИЖЕ средней: {Fore.RED}{little}{Style.RESET_ALL}')
