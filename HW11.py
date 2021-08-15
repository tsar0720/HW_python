"""
Напишите функцию letters_range, которая ведет себя
похожим на range образом, однако в качестве start и
stop принимает не числа, а буквы латинского алфавита
(в качестве step принимает целое число) и возращает
не перечисление чисел, а список букв, начиная с
указанной в качестве start, до указанной в качестве
stop с шагом step (по умолчанию равным 1).
"""


def letters_range(start, stop, step=1):
    start = ord(start) # получаю символ в числовом представлении
    stop = ord(stop)   # получаю символ в числовом представлении
    mas = list()
    for i in range(start, stop, step):
        mas.append(chr(i)) # получаю символ из числового представления и добавляю в список
    return mas


print(letters_range('b', 'w', 2))
print(letters_range('a', 'g'))
print(letters_range('g', 'p'))
print(letters_range('p', 'g', -2))
print(letters_range('a','a'))