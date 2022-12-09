'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
 Все конфеты оппонента достаются сделавшему последний ход.
 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
from random import randint

def input_data(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, попробуй еще раз: "))
    return x


def p_vs_p(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
x = randint(1, 2)
if x == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
count = 0
counter1 = 0
counter2 = 0

while value > 28:
    if count == 0:
        k = input_data(player1)
        counter1 += k
        value -= k
        count = 1
        p_vs_p(player1, k, counter1, value)
    else:
        k = input_data(player2)
        counter2 += k
        value -= k
        count = 0
        p_vs_p(player2, k, counter2, value)

if count == 0:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")