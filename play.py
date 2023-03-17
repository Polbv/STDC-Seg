import os
import numpy as np
import cv2
def play(videopath):
    stream=cv2.VideoCapture(videopath)
    print("press q to stop the video from playing press any key to exit asfter pausing")
    while (stream.isOpened()):
        ret,frame=stream.read()
        if (ret== True):
            cv2.imshow('video',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else : break
   
    cv2.waitKey(0)
    stream.release()