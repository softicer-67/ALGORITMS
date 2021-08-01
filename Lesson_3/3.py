'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random


arr = [random.randint(1, 1000) for i in range(10)]
mini = min(arr)
maxi = max(arr)
min_index = arr.index(mini)
max_index = arr.index(maxi)
print('Минимальное число в массиве:', mini)
print('Максимальное число в массиве:', maxi)
print(arr, 'Начальный массив')
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(arr, 'Измененный массив')
