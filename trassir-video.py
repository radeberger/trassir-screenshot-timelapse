import requests
import json
import urllib.request
import ssl
import urllib3
import datetime

urllib3.disable_warnings()
path = "f:\\majino-screenshots\\save_video18.avi"
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
start_date = int(start_date.timestamp()*1000000)
with urllib.request.urlopen("https://172.18.16.253:8080/login?password=SdKpa$$") as url1:
    sid = url1.read().decode("utf-8")
sid = sid.split()[-2].replace("\"", "")
print(sid)
# получаем sid
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data = {"resource_guid": guid,
        "start_ts": start_date,
        "end_ts": start_date+record_dur,
        "is_hardware": 0,
        "prefer_substream": 0}

url1 = "https://172.18.16.253:8080/jit-export-create-task?sid=" + sid
answer = requests.post(url1, data=json.dumps(data), headers=headers, verify=False)
print(answer)
response = str(answer.json())
print(response)
task_id = response.split()[-1].replace("\'", "").replace("}", "")
print(task_id)
# получаем task-id
f = open(path, 'wb')

f.write(urllib.request.urlopen(
    "https://172.18.16.253:8080/jit-export-download?sid=" + sid + "&task_id=" + task_id).read())
f.close()