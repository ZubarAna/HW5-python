'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
# test = фабвф мама абв мыла абвг раму габв

text = list(map(str, input("Введите текст через пробел: \n").split()))
print(f'Исходная строка: {" ".join(text)}')
new_text = list(filter(lambda x: not 'абв' in x, text))

print(f'Получившаяся строка: {" ".join(new_text)}')
