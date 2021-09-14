import os
import sys

path = "f:\\Trassir\\screenshots\\"
import datetime
from datetime import timedelta
import urllib.request
import ssl
#172.31.176.3
#172.18.16.253 Сходня

with urllib.request.urlopen("https://172.18.16.253:8080/login?password=SdKpa$$",
                            context=ssl._create_unverified_context()) as url:
    sid = url.read().decode("utf-8")
# получаем идентификатор сессии, он живет по умолчанию 15 минут или вечно при продолжающихся обращениях
print(sid)
if sid.split()[-2].replace("\"", "") == "protection":
    print("Превышено количество подключений к серверу!")
    sys.exit()

print("Введите guid канала")
guid = str(input())
# guid канала из Трассира
print("Введите год начала записи, например, 2021")
start_year = int(input())
print("Введите месяц начала записи, например, 1")
start_month = int(input())
print("Введите день начала записи, например, 2")
start_day = int(input())
print("Введите час начала записи, например, 0")
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
print("Введите час окончания записи, например, 9")
end_hour = int(input())
print("Введите минуту окончания записи, например, 5")
end_minute = int(input())
end_second = 0
print("Введите интервал между кадрами в секундах")
interval = int(input())
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
    f.write(urllib.request.urlopen(
        "https://172.18.16.253:8080/screenshot/" + guid + "?timestamp=" + timestamp + "&sid=" + sid.split()[-2].replace(
            "\"", ""),
        context=ssl._create_unverified_context()).read())
    f.close()
    # пишем скриншот в файл

    start_date = start_date + timedelta(seconds=interval)
    print(start_date)
    # шаг скриншотов задаем в секундах
    i = i + 1

os.system("ffmpeg -framerate 10 -f image2 -i " + path + "\\" + "image%6d.jpg -qscale:v 3 arm_high.avi")
# делаем таймлапс
