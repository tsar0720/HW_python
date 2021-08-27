"""
Написать программу, которая будет считывать из файла gps координаты,
и формировать текстовое описание объекта и ссылку на google maps.
Пример:

Input data: 60,01';30,19'
Output data:
Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
"""

from geopy.geocoders import Nominatim
import re


def find_coordinates(file_name = "coordinates.txt") :
    with open(file_name, "r") as coordinates:
        for coodinate in coordinates:

            if "'" in coodinate:
                input_data = re.sub("['|;]", " ", coodinate).replace(",", ".")

                # присваиваю широту и долготу переменным
                left, right = [float(x) for x in input_data.split()]

                # Для последующих вычислений нужна дробная и целая часть
                hours1 = int(left)
                min1 = (left - hours1) * 100

                # Для последующих вычислений нужна дробная и целая часть
                hours2 = int(right)
                min2 = (right - hours2) * 100

                # преобразовываю в десятичное представление
                decimal_degree1 = hours1 + min1 / 60  # + sec/3600
                decimal_degree2 = hours2 + min2 / 60

                # использую модуль geopy
                geolocator = Nominatim(user_agent="test1")
                location = geolocator.reverse(str(decimal_degree1) + "," + str(decimal_degree2))
                print("Output data:")
                print(f"Location: {location.address}")
                print("Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=" + str(
                    location.latitude) + "," + str(
                    location.longitude))
            else:
                # разбиваю через пробелы и записываю в переменные
                right, left = coodinate.split(" ")
                # использую модуль geopy
                geolocator = Nominatim(user_agent="test")
                location = geolocator.reverse(right + "," + left)
                print("Output data:")
                print(f"Location: {location.address}")
                print("Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=" + str(location.latitude) + "," + str(
                    location.longitude))



