"""
Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 .......
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


num = int(input("Введите число: "))
print(fib(num))
