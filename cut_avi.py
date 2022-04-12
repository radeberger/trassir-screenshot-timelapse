from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("video-sutki.avi")
# getting only first 5 seconds
clip = clip.subclip(10, 100)
# showing clip
#clip.ipython_display(width = 720)
clip.write_videofile("cutted.mp4")