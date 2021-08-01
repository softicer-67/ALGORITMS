'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random


arr = [random.randint(1, 4) for i in range(20)]

# для проверки
print('массив', arr, '\n')
for i in set(arr):
    print('число', i, 'в массиве', arr.count(i), 'шт.')

# результат
print('\nЧисло:', max(arr, key=arr.count), 'встречается в массиве чаще всего')
