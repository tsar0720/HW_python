"""
1. Количество пользователей, использующих все имеющиеся
интерпретаторы-оболочки.
( /bin/bash - 8 ; /bin/false - 11 ; ... )
"""

"""
Открываю файл на чтение, считываю построчно, в каждой строке беру последнее значение после двоеточий
Добавляю все в список
Выбираю уникальные значения с помощью set и создаю из этого список
Перебираю список по уникальным значениям и доабвляю каждое значени в словарь
Словарь: Уникальное значение = Подсчитать сколько всего встречается таких значений в первом списке.
"""
shells = []
with open('passwd.txt', 'r') as passwd:
    for line in passwd:
        shells.append(line.strip().split(':')[-1])

unique_shells = list(set(shells))

count_shells = dict()
for i in range(len(unique_shells)):
    count_shells[unique_shells[i]] = shells.count(unique_shells[i])

print("Количество оболочек: ")
print(count_shells)