'''
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''
import cProfile


numbers = '22', '33', '555', '99', '1111',


def sum_numbers(numbers):
    summa = 0
    for item in numbers:
        summa += int(item)
    return summa


max_number = 0
max_sum = 0
for i in numbers:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'У числа {max_number} наибольшая сумма цифр = {max_sum}')


def main():
    num = 3 ** 100000
    res_count = sum_numbers(str(num))
    res_sum = sum_numbers(str(num))


if __name__ == '__main__':
    cProfile.run('main()')

'''
У числа 99 наибольшая сумма цифр = 18
         6 function calls in 0.073 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.011    0.005    0.011    0.005 1.py:11(sum_numbers)
        1    0.062    0.062    0.073    0.073 1.py:28(main)
        1    0.000    0.000    0.073    0.073 <string>:1(<module>)
        1    0.000    0.000    0.073    0.073 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
