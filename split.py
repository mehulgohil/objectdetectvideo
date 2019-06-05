import cv2
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

cam = cv2.VideoCapture("sample.mp4")
clip = VideoFileClip("sample.mp4")
print(clip.duration)

fps = cam.get(cv2.CAP_PROP_FPS)

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error: Creating directory of data')

currentframe = 0
ret = True

while(ret):
    ret, frame = cam.read()
    if currentframe % fps == 0:
        name = './data/frame' + str(currentframe) + '.jpg'
        cv2.imwrite(name,frame)

    currentframe+=1

cam.release()
cv2.destroyAllWindows()
