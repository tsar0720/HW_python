"""
Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести текст.
2. Проверяет и, если возможно, преобразовывает полученный текст в число,
используя рекурсивную функцию.
Если число четное - делит его на 2 и выводит результат.
Если число нечетное - умножает на 3 и прибавляет 1.
После чего ждет следующего ввода.
3.При получении в качестве вводных данных 'cancel' завершает свою работу.
Пример:

-> Привет123
Не удалось преобразовать введенный текст в число.
-> 2
1
-> 3
10
-> Два
Не удалось преобразовать введенный текст в число.
-> cancel
Bye!
"""


def strToInt(s):
    if s:
        # s = 123 unicode(3) = 51
        # unicode(0) = 48 => 51-48 = 3
        # s[:-1] = 12
        # 10 * 12 = 120
        # 120 + 3 = integer 123
        return (ord(s[-1]) - ord('0')) + 10 * strToInt(s[:-1])
    else:
        return 0


while (True):
    str = input("Введите число: ")
    if str.isdigit():
        result = strToInt(str)
        if result % 2 == 0:
            print(int(result / 2))
        else:
            print((result * 3) + 1)
    elif str == 'cancel':
        break
    else:
        print("Не удалось преобразовать введенный текст в число.")