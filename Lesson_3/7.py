'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''


import random

arr = [random.randint(1, 99) for _ in range(11)]
print('\n', arr)

sort_arr = sorted(arr)
print(' Два наименьших элемента в массиве', sort_arr[0], 'и', sort_arr[1], '- легкий вариант через  сортировку')


mini_1 = min(arr)
min_ind = arr.index(mini_1)
new_arr = arr[:]
del new_arr[min_ind]
mini_2 = min(new_arr)
print('\n', arr)
print(' Два наименьших элемента в массиве', mini_1, 'и', mini_2, '- вариант с копией основного массива ;)')
