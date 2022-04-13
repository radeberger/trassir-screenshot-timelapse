import requests
import json
import urllib.request
import ssl
import urllib3
import datetime
import glob, os

os.chdir("f:\\trassir-video\\")

for file in glob.glob("*.avi"):
    os.remove(file)
open("avi-list.txt", "w").close() #clear file

urllib3.disable_warnings()
path = "f:\\trassir-video\\"
# ssl._create_default_https_context = ssl._create_unverified_context
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
# избавляемся от ошибки ssl
print("Введите guid канала")
guid = input()
#guid канала из Трассира
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
start_date = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute, start_second)
print("Введите продолжительность записи в минутах (от 1 до 30)")
record_dur = int(input())*60*1000000
start_date = int(start_date.timestamp()*1000000 + 3*3600*1000000)
print("Сколько часов?")
hour_count = int(input())
count = 0
while count <= hour_count:
    with urllib.request.urlopen("https://172.31.176.3:8080/login?password=SdKpa$$") as url1:
        sid = url1.read().decode("utf-8")
    sid = sid.split()[-2].replace("\"", "")
    print("sid ", sid)
    # получаем sid
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    data = {"resource_guid": guid,
            "start_ts": start_date,
            "end_ts": start_date + record_dur,
            "is_hardware": 0,
            "prefer_substream": 0}

    url1 = "https://172.31.176.3:8080/jit-export-create-task?sid=" + sid
    answer = requests.post(url1, data=json.dumps(data), headers=headers, verify=False)
    # print(answer)
    response = str(answer.json())
    print(response)
    task_id = response.split()[-1].replace("\'", "").replace("}", "")
    # print("task id ", task_id)
    # получаем task-id
    f = open(path + str(count) + ".avi", 'wb')

    f.write(urllib.request.urlopen(
        "https://172.31.176.3:8080/jit-export-download?sid=" + sid + "&task_id=" + task_id).read())
    f.close()
    url2 = "https://172.31.176.3:8080/jit-export-cancel-task?sid=" + sid + "&task_id=" + task_id
    # !!!!!!!!!!!!!!!!!!!!!!!!
    answer = requests.get(url2, verify=False)
    response = str(answer.json())
    print("сброс задачи")
    print(response)
    # сброс задачи
    start_date = start_date + 3600*1000000
    count = count + 1

os.chdir("f:\\trassir-video\\")
f = open('avi-list.txt', 'w')
for file in glob.glob("*.avi"):
    if os.path.getsize(file) != 0:
        f.write('file ' + file + '\n')
        print(file)
f.close()

os.system("ffmpeg -f concat -safe 0 -i avi-list.txt concat_video.avi")