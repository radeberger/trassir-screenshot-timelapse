import urllib.request
import ssl


with urllib.request.urlopen("https://172.31.176.3:8080/login?password=SdKpa$$", context=ssl._create_unverified_context()) as url:
    sid = url.read().decode("utf-8")
    print(sid.split()[-2].replace("\"", ""))
    #)
    #sid2 = url.read().decode("utf-8")
    # I'm guessing this would output the html source code ?
    # sid2 = sid
if sid.split()[-2].replace("\"", "") == "protection":
    print("Превышено количество подключений к серверу!")
    #print(sid2).split()[-2]

with urllib.request.urlopen("https://172.31.176.3:8080/objects/?password=SdKpa$$", context=ssl._create_unverified_context()) as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s.decode("utf-8"))
    #print(type(s))
