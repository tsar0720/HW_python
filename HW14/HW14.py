"""
Создать сотрудника Mary, пользуясь классом
Employee и перенести его в другую программу,
используя модуль Pickle и файловую систему.
Узнать про + и - модуля Pickle.
"""
import pickle

# Создал базовый класс
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Унаследовал все поля от родительского класса
class Mary(Employee):

    # Добавил метод для класса
    def tell_about_you(self):
        return (f"Hello my name is {self.name}, and i am {self.age} years old")

# Создал объект класса
mary = Mary("Mary", 22)

# Применив модуль pickle сделал сериализацию записав байты в текстовый файл с именем data.pickle
with open('data.pickle', 'wb') as f:
    pickle.dump(mary, f)
f.close()

print(f"Mary from MAIN program: {mary.tell_about_you()}")

