"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

a, b = [i.upper() for i in input('Введите 2 буквы латинского алфавита слитно: ')]

# генерим алфавит
alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Определяем какая буква по счету
letter1 = alpha.index(a) + 1
letter2 = alpha.index(b) + 1

# подсчитываем колличество между бувами
interval = letter2 - letter1 - 1

# проверка на случай если буквы указаны не по возрастанию
if letter2 < letter1:
    interval = letter1 - letter2 - 1

# исправим на правильное написание слов
text = []
if interval == 1 or interval == 21:
    text = 'буква'
elif interval == 2 or interval == 3 or interval == 4 or interval == 22 or interval == 23 or interval == 24:
    text = 'буквы'
else:
    text = 'букв'

print('Первая буква стоит на', letter1, 'месте')
print('Вторая буква стоит на', letter2, 'месте')
print('Между ними', interval, text)
