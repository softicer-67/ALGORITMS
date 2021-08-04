'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

from random import randint


def bubble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


N = 20
arr = []
for i in range(N):
    arr.append(randint(-100, 100))

print(arr)
bubble(arr)
print(arr)
