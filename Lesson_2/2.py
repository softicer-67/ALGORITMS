'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''


number = input('Введите число: ')
even = 0
odd = 0
num_even = []
num_odd = []
for f in number:
    i = int(f)
    if i % 2 == 0:
        num_even.append(i)
        even += 1
    else:
        num_odd.append(i)
        odd += 1
print(f'У числа {number}: {even} четных {num_even} и {odd} нечетные {num_odd}')
