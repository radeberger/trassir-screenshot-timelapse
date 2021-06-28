import os
os.system("ffmpeg -f concat -safe 0 -i avi-list.txt concat_video.avi")
