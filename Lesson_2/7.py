'''
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''
from colorama import Fore, Style

n = 1
while n != 200:
    left = 0
    for i in range(1, n + 1):
        left += i
    right = n * (n + 1) // 2
    n += 1
    if left == right:
        res = True
    else:
        res = False
    print('=' * 10)
    print(left)
    print(right)
    print(f'{Fore.GREEN}{res}!{Style.RESET_ALL}')
