"""
Напишите функцию, которая переводит значения показаний
температуры из Цельсия в Фаренгейт и наоборот.
"""


def farenheit_to_celsium_and_back(value, conversion_to):
    if conversion_to == 'F' or conversion_to == 'f':
        return (9/5) * value + 32
    if conversion_to == "C" or conversion_to == 'c':
        return (5/9) * (value - 32)


print(f"12 градусов по цельсию равно {farenheit_to_celsium_and_back(12, 'f')} \
      градусов по фаренгейту.")