'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
'''

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
