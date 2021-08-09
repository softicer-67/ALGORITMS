'''
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''

import hashlib

s = 'hello world'

sum_substring = set()

for i in range(len(s)):
    for j in range(len(s), i, -1):
        hash_str = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) -1} различных подстрок в строке {s}')
