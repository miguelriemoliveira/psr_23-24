#!/usr/bin/env python3 
import argparse
from copy import deepcopy
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style


def main():

    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    capture = cv2.VideoCapture('./areyouspeaking.mp4')
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    # cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('mask_edges',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('mask_mouth',cv2.WINDOW_NORMAL)

    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    image_gray_prev = None
    while True:
        _, image_rgb = capture.read()  # get an image from the camera
        height, width, nc = image_rgb.shape
        image_gui = deepcopy(image_rgb)
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
        

        # Face detection
        faces = face_classifier.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

        # Create a mask of the face
        mask = np.zeros((height, width), dtype=np.uint8)
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

        # Paint detected face in green 
        b, g, r = cv2.split(image_rgb)

        g = g.astype(float)
        g[mask.astype(bool)] = g[mask.astype(bool)] * 1.5
        g[g>255] = 255 # saturation on 255
        g = g.astype(np.uint8)

        image_gui = cv2.merge([b,g,r])

        # Ex 3b) Draw edges in red

        # Detect edges
        mask_edges = cv2.Canny(image_gray,50,100)
        mask_edges = cv2.dilate(mask_edges, np.ones((5, 5), np.uint8), iterations=1) 

        for face in faces:
            x, y, w, h = face
            cv2.rectangle(mask_edges, (x, y), (x + w, y + h), 0, -1)
 
        # Paint edges in red
        b, g, r = cv2.split(image_gui)

        r = r.astype(float)
        r[mask_edges.astype(bool)] = r[mask_edges.astype(bool)] * 1.5
        r[r>255] = 255 # saturation on 255
        r = r.astype(np.uint8)

        image_gui = cv2.merge([b,g,r])

        # get mouth area

        selected_face = faces[0]
        for face in faces:
            x, y, w, h = face
            if w > selected_face[2]:
                selected_face = face

        x, y, w, h = selected_face
        y = int(y + 2*h/3)
        h = int(h/3)

        cv2.rectangle(image_gui, (x, y), (x + w, y + h), (0, 255, 255), 9)

        mask_mouth = np.zeros((height, width), dtype=np.uint8)
        cv2.rectangle(mask_mouth, (x, y), (x + w, y + h), 255, -1)

        # Detect motion
        if image_gray_prev is not None:
            diff = cv2.absdiff(image_gray, image_gray_prev)
            diff[np.logical_not(mask_mouth)] = 0
            
            soma = np.sum(diff)
            print('soma ' + str(soma))

            if soma > 300000:
                print('You are speaking!')

                image_gui = cv2.putText(image_gui, 'You are speaking!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                                1, (0,0,255), 2, cv2.LINE_AA) 
            else:
                print('You are silent!')
                image_gui = cv2.putText(image_gui, 'You are silent!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                                1, (255,0,0), 2, cv2.LINE_AA) 


        # -----------------------------------------------
        # Visualization 
        # -----------------------------------------------
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.imshow(window_name, image_gui)
        # cv2.imshow('mask', mask)
        # cv2.imshow('mask_edges', mask_edges)
        # cv2.imshow('mask_mouth', mask_mouth)

        key = cv2.waitKey(10)

        if key == 113: # q
            exit(0)

        image_gray_prev = image_gray

    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------

if __name__ == '__main__':
    main()