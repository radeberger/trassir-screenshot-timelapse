import requests
import json
import urllib.request
import ssl
import urllib3
import datetime
import time

urllib3.disable_warnings()
path = "C:\\Users\\usr6243828\\PycharmProjects\\Trassir\\save_video.avi"
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
with urllib.request.urlopen("https://172.31.176.3:8080/login?password=SdKpa$$") as url1:
    sid = url1.read().decode("utf-8")
sid = sid.split()[-2].replace("\"", "")
print(sid)
print(guid)
# получаем sid
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data = {"resource_guid": guid,
        "start_ts": 1623831230000000,
        "end_ts": 1623831350000000,
                  1622948760000000
        "is_hardware": 0,
        "prefer_substream": 0}

url1 = "https://172.31.176.3:8080/jit-export-create-task?sid=" + sid
answer = requests.post(url1, data=json.dumps(data), headers=headers, verify=False)
print(answer)
response = str(answer.json())
print(response)
task_id = response.split()[-1].replace("\'", "").replace("}", "")
print(task_id)
print(int(start_date.timestamp()*1000000))