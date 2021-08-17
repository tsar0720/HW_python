"""
Напишите программу, которая читает данные из файлов
/etc/passwd и /etc/group на вашей системе и выводит
следующую информацию в файл output.txt:

2. Для всех групп в системе - UIDы пользователей
состоящих в этих группах.
( root:1, sudo:1001,1002,1003, ...)
"""

# Беру из файла пользователя и его группу
# обращаюсь к каждой строке и беру значение в нужных позициях добавляю в словарь
user__and_his_group = dict()
with open('passwd.txt', 'r') as passwd:
    for line in passwd:
        user__and_his_group[line.strip().split(':')[0]] = line.strip().split(':')[2]
print(user__and_his_group)

# Беру из файла группу и пользователя которые входят в группу
# обращаюсь к каждой строке и беру значение в нужных позициях добавляю в словарь
users_included_in_the_group = dict()
with open('group.txt', 'r') as group:
    for line in group:
        users_included_in_the_group[line.strip().split(':')[0]] = line.strip().split(':')[3]

# Получаю значения в словаре у которых не пустое поле с пользователями
users_included_in_the_group = {k: v for k, v in users_included_in_the_group.items() if v != ''}

print(users_included_in_the_group)


# Прохожусь циклом по словарю с группами у которых поле не пустое
# Добавляю в результирующий словарь по ключу группу, и айди пользователя из первого словаря
result = dict()
for key, value in users_included_in_the_group.items():
    result[key] = user__and_his_group[value]

print("Результат: ", result)

