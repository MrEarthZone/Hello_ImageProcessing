import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    upper = np.array([150, 255, 200])
    lower = np.array([0, 0, 0])

    mask = cv2.inRange(hsv,lower,upper)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('image', frame)
    cv2.imshow('image2', mask)
    cv2.imshow('image3', res)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()