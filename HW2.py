'''
Встроенная функция input позволяет ожидать и возвращать данные из стандартного
ввода в виде строк (весь введенный пользователем текст до нажатия им enter).
Используя данную функцию, напишите программу, которая:

1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
слоги, числа или их комбинации, разделенные пробелом.
2. Считывает строку с текстом, и разбивает его на элементы списка, считая
пробел символом разделителя.
3. Печатает этот же список элементов (через пробел), однако с удаленными
дубликатами.
'''

input_string = input("Введите любые слова, слоги, числа или их комбинации, разделенные пробелом: ")
result_list = list(input_string.split())
result_set = set(input_string.split())
print(f'List result: {" ".join(result_list)}')
print(f'Set result:  {" ".join(result_set)}')
