from __future__ import print_function
import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
from imutils import paths
import argparse
import imutils
import threading

result = 0
Hello = 0

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()

def video_detect():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 1)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            counter = 0
            (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),padding=(8, 8), scale=1.05)
            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
            for (xA, yA, xB, yB) in pick:
                counter += 1
                print(counter)
                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
            if (counter == 0):
                print(counter)
            out.write(frame)
            return counter
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

#setInterval(video_detect, 1)
result = video_detect()
print(result)

def capacity():
    return result
#print("This is the return value: ",capacity())
x = str(capacity())
print(x)
print(type(x))





