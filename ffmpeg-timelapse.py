import os
import sys
path = "f:\\Trassir\\screenshots\\"

os.system("ffmpeg -framerate 15 -f image2 -i " + path + "image%6d.jpg -qscale:v 3  f:\\Trassir\\torez-sutki.avi")
# делаем таймлапс
#os.system("ffmpeg -framerate 15 -f image2 -i F:\\Trassir\\1\\*.jpg -qscale:v 3 f:\\Trassir\\torez-sutki.avi")

#os.system("ffmpeg -framerate 10 -f image2 -i " + path + "\\" + "image%6d.jpg -qscale:v 3 arm_high.avi")

#"F:\Trassir\screenshots\image003482.jpg"