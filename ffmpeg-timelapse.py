import os


os.system("ffmpeg -framerate 15 -f image2 -i  f:\\Trassir\\20210706081000\\image%6d.jpg -qscale:v 3  f:\\Trassir\\timelapse.avi")
# делаем таймлапс
