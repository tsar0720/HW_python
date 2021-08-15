"""
Задача
Вычислить число шагов для числа n, согласно гипотезе
Коллатца необходимых для достижения этим числом единицы.

"""

num = int(input("Введите число: "))
print(num)
counter = 0
while True:

    if num == 1:
        break
    elif num % 2 == 0:
        num = num / 2
        counter += 1
        print(int(num))
    else:
        num = (num * 3) + 1
        counter += 1
        print(int(num))

print(f"Всего получаем {counter} шагов.")
