"""
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)

Напишите программу, которая решает описанную выше задачу и печатает ответ.
"""

# список для двоичных цифр
binary = list()

# список для десятичных цифр
decimal = list()

# словарь для соответствий
d = dict()

# итерируюсь, привожу каждое число к бинарному виду
# добавляю бинарные и десятичные числа в список
for i in range(1, 1_000_000):
    a = bin(i).replace("0b", "")
    binary.append(a)
    decimal.append(str(i))

# проверяю число полиндром или нет с помощью взятия каждого числа, инвертируя его и сравнивая тем которое в списке, 
# если при перевороте оно такое же как и то что лежит в списке, то число полиндром 
for i in range(len(decimal)):
    if (binary[i][::-1] == binary[i]) and (decimal[i][::-1] == decimal[i]):
        d[binary[i]] = decimal[i]

print(d)
