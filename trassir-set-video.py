import requests
import json
import urllib.request
import ssl
import urllib3
import datetime
import glob, os
#from datetime import timedelta

urllib3.disable_warnings()

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
print("Введите год окончания записи, например, 2021")
end_year = int(input())
print("Введите месяц окончания записи, например, 2")
end_month = int(input())
print("Введите день окончания записи, например, 2")
end_day = int(input())
print("Введите час окончания записи, например, 10 ")
end_hour = int(input())
print("Введите минуту окончания записи, например, 5")
end_minute = int(input())
end_second = 0
start_date = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute, start_second)
end_date = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)
print("Введите продолжительность записи в секундах (от 1 до 1800)")
record_dur = int(input())*1000000
start_date = int(start_date.timestamp()*1000000 + 3*3600*1000000)
end_date = int(end_date.timestamp()*1000000 + 3*3600*1000000)
#+3 часа, почему то съезжает время на 3 часа назад, timezone???
print("Введите частоту записи в часах (1-каждый час, 2 - каждые 2 часа и т.д.")
record_quant = int(input())*3600*1000000

while start_date <= end_date:
    #with urllib.request.urlopen("https://172.18.16.253:8080/login?password=SdKpa$$") as url1:
    with urllib.request.urlopen("https://172.31.176.3:8080/login?password=SdKpa$$") as url1:
        sid = url1.read().decode("utf-8")
    sid = sid.split()[-2].replace("\"", "")
    print("------------------")
    print(sid)
    # получаем sid

    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    data = {"resource_guid": guid,
            "start_ts": start_date,
            "end_ts": start_date + record_dur,
            "is_hardware": 0,
            "prefer_substream": 0}
    #print(record_quant/1000000/3600)
    #url1 = "https://172.18.16.253:8080/jit-export-create-task?sid=" + sid
    url1 = "https://172.31.176.3:8080/jit-export-create-task?sid=" + sid
    answer = requests.post(url1, data=json.dumps(data), headers=headers, verify=False)
    print(answer)
    response = str(answer.json())
    print(response)
    task_id = response.split()[-1].replace("\'", "").replace("}", "")
    print(task_id)
    # получаем task-id
    try:
        path = "C:\\Users\\usr6243828\\PycharmProjects\\Trassir\\" + str(start_date) + ".avi"
        f = open(path, 'wb')
        #f.write(urllib.request.urlopen("https://172.18.16.253/jit-export-download?sid=" + sid + "&task_id=" + task_id).read())
        f.write(urllib.request.urlopen("https://172.31.176.3/jit-export-download?sid=" + sid + "&task_id=" + task_id).read())
        f.close()
        #запись файла
        #url2 = "https://172.18.16.253:8080/jit-export-cancel-task?sid=" + sid + "&task_id=" + task_id
        url2 = "https://172.31.176.3:8080/jit-export-cancel-task?sid=" + sid + "&task_id=" + task_id
        #!!!!!!!!!!!!!!!!!!!!!!!!
        answer = requests.get(url2, verify=False)
        #сброс задачи
        print(answer)
    except Exception:
        pass
    #try-except т.к. валится bad request, скорее всего из-за обрывов в архиве
    start_date = start_date + record_quant
os.chdir("C:\\Users\\usr6243828\\PycharmProjects\\Trassir\\")
f = open('avi-list.txt', 'w')
for file in glob.glob("*.avi"):
    if os.path.getsize(file) != 0:
        f.write('file ' + file + '\n')
        print(file)
f.close()

os.system("ffmpeg -f concat -safe 0 -i avi-list.txt concat_video.avi")