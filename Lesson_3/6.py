'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

arr = [random.randint(1, 99) for _ in range(11)]
print('\n', arr)

mini = min(arr)
maxi = max(arr)
min_ind = arr.index(mini)
max_ind = arr.index(maxi)
print('\n Минимальный элемент', mini, 'с индексом', min_ind)
print(' Максимальный элемент', maxi, 'с индексом', max_ind)

res = 0
if min_ind < max_ind:
    res += sum(arr[min_ind + 1:max_ind])
else:
    res += sum(arr[max_ind + 1:min_ind])
print('\n Сумма элементов, находящихся между минимальным и максимальным элементами =', res)
