'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

num = []

for i in range(4):
    num.append([])
    num[i].extend([random.randint(0, 99) for _ in range(8)])

min_list = []
min_list.extend(num[0])

for string in num:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('\tМинимальные числа в столбцах\n')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы:', min_list[0])
