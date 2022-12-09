'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''
# test input: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# output: 12W1B12W3B24W1B14W
with open('Task4_RLE_coding', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()
print(my_text)
def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res
text_coding = coding(my_text)
text_decoding = decoding(coding(my_text))
with open('Task4_RLE_decoding', 'w', encoding='UTF-8') as file:
    file.write(f'{text_coding} \n {text_decoding}')
