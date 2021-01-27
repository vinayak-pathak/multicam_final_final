#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:52:01 2021

@author: vinayakpathak
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

# cap3 = cv2.VideoCapture(3)
# cap4 = cv2.VideoCapture(4)

if (cap.isOpened() == False):
    print("Unable to read camera feed")
if (cap2.isOpened() == False):
    print("Unable to read camera feed")
# if (cap3.isOpened() == False):
# print("Unable to read camera feed")
# if (cap4.isOpened() == False):
# print("Unable to read camera feed")
# imS = cv2.resize(im, (960, 540))
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# frame_width2 = int(cap2.get(3))
# frame_height2 = int(cap2.get(4))

# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while (True):

    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    # ret3, frame3 = cap.read()
    # ret4, frame4 = cap2.read()

    # imS1 = cv2.resize(frame, (480, 270))
    # imS2 = cv2.resize(frame2, (480, 270))
    # imS3 = cv2.resize(frame3, (480, 270))
    # imS4 = cv2.resize(frame4, (480, 270))

    if ret == True or ret2 == True:  # or ret3==True:

        # out.write(frame)

        cv2.imshow('frame', frame)
        cv2.imshow('frame2', frame2)
        # cv2.imshow('frame3',imS3)
        # cv2.imshow('frame4',ims4)

        # Press Q on keyboard to stop recording

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:

        break

cap.release()
cap2.release()
# cap3.release()
# cap4.release()

# out.release()
cv2.destroyAllWindows()



