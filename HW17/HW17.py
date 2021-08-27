"""
Написать скрипт, который будет вытаскивать gps данные
из фотографии (jpg файл) и передавать их на вход программе
из hw16.txt
"""
"""
pip3 install piexif
pip3 install gpsphoto
python3 -m pip install --upgrade Pillow
"""
from GPSPhoto import gpsphoto
from HW16 import HW16

# использую модуль GPSPhoto
data_one = gpsphoto.getGPSData('one.jpg')
data_two = gpsphoto.getGPSData('two.jpg')

# помещаю координаты в словарь
dict_coordinates = {data_one['Latitude'] : data_one['Longitude'],
                    data_two['Latitude']: data_two['Longitude']}

# сохраняю в файл
with open("coordinates_from_photo.txt", "w") as file:
    for key, value in dict_coordinates.items():
        file.write(str(key) + " " + str(value) + "\n")

# запускаю метод из HW16
HW16.find_coordinates("coordinates_from_photo.txt")