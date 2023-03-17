import os
import numpy as np
import cv2
from play import play

stream=cv2.VideoCapture('./video.mp4')
f=cv2.VideoWriter_fourcc(*'mp4v')
vidoutput=cv2.VideoWriter("outputvideo.mp4",f,30,(368,640))#First width then height. (the opposite from what np.shape outputs)
while (stream.isOpened()):
    ret,frame=stream.read()
    print(np.shape(frame))
    if (ret== True):
        cv2.rectangle(frame,(50,100),(100,200),(0,0,255),5)
        vidoutput.write(frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else : break
   
cv2.waitKey(0)
vidoutput.release()
stream.release()
cv2.destroyAllWindows()
videopath='./outputvideo.mp4'
play(videopath)


