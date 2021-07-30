import http.client
import os
import sys

path = "F:\\Trassir\\"
import datetime
from datetime import timedelta
import urllib.request
import ssl

with urllib.request.urlopen("https://172.31.176.3:8080/login?password=SdKpa$$",
                            context=ssl._create_unverified_context()) as url:
    sid = url.read().decode("utf-8")
# получаем идентификатор сессии, он живет по умолчанию 15 минут или вечно при продолжающихся обращениях

if sid.split()[-2].replace("\"", "") == "protection":
    print("Превышено количество подключений к серверу!")
    sys.exit()

print("Введите guid канала")
guid = str(input())

print("Введите интервал между кадрами в секундах")
interval = int(input())
print("Вырезаем ночь (y/n)?")
cut_night = input()
if cut_night == ("y" or "Y"):
    print("Введите час начала ночи")
    night_start = int(input())
    print("Введите час окончания ночи")
    night_end = int(input())

print("Введите год начала записи, например, 2021")
start_year = int(input())
print("Введите месяц начала записи, например, 1")
start_month = int(input())
print("Введите день начала записи, например, 2")
start_day = int(input())
if cut_night == ("y" or "Y"):
    print("Введите час начала записи, нe больше ", night_start-1)
else:
    print("Введите час начала записи, например,18 ")
start_hour = int(input())
print("Введите минуту начала записи, например, 1")
start_minute = int(input())
start_second = 0
print("Введите год окончания записи, например, 2021")
end_year = int(input())
print("Введите месяц окончания записи, например, 2")
end_month = int(input())
print("Введите день окончания записи, например, 2")
end_day = int(input())
if cut_night == ("y" or "Y"):
    print("Введите час окончания записи, не меньше ", night_end)
else:
    print("Введите час окончания записи, например, 10 ")

end_hour = int(input())
print("Введите минуту окончания записи, например, 5")
end_minute = int(input())
end_second = 0

start_date = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute, start_second)
end_date = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)

path = path + str(start_date.strftime("%Y%m%d")) + str(start_date.strftime("%H%M%S"))
os.mkdir(path)
i = 0

while start_date <= end_date:


    timestamp = str(start_date.strftime("%Y%m%d")) + "T" + str(start_date.strftime("%H%M%S"))
    # заводим метку времени для обращения к серверу
    f = open(path + "\\" + "image" + str(i).zfill(6) + '.jpg', 'wb')
    # в имени файла добавляем нули - у ffmpeg проблемы с шаблонами под виндой
    try:
        f.write(urllib.request.urlopen(
        "https://172.31.176.3:8080/screenshot/" + guid + "?timestamp=" + timestamp + "&sid=" + sid.split()[-2].replace(
            "\"", ""),
        context=ssl._create_unverified_context()).read())

        # пишем скриншот в файл
    except http.client.IncompleteRead as error:
        print(error)
    finally:
        f.close()
        start_date = start_date + timedelta(seconds=interval)
    # шаг скриншотов задаем в секундах
        if cut_night == ("y" or "Y"):
            if start_date.hour >= night_start:
                start_date = start_date + timedelta(seconds=(24 - start_date.hour + night_end) * 3600)
    # если вырезаем ночь, то
    #условие определения - не влезли ли мы в ночь, если да, то прыг на конец ночи

        i = i + 1
        print(start_date)

os.system("ffmpeg -framerate 10 -f image2 -i " + path + "\\" + "image%6d.jpg -qscale:v 3  -s 1920x1128 f:\\trassir\\timelapse.avi")
# делаем таймлапс
