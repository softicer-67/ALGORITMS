'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

from random import randint


def sort(array):
    res = []
    new_arr = arr[:]
    for _ in range(len(new_arr)):
        mini = min(new_arr)
        mini_index = new_arr.index(mini)
        res.append(mini)
        del new_arr[mini_index]
    return res


N = 20
arr = []
for i in range(N):
    arr.append(randint(0, 50))

print(arr)
print(sort(arr))
