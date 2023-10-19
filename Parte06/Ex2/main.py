#!/usr/bin/env python3 
import argparse
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style


def mouseCallback(event, x, y, flags, *userdata, image_rgb, drawing_data):

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_data['pencil_down'] = True
        print(Fore.BLUE + 'pencil_down set to True' + Style.RESET_ALL)
        
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing_data['pencil_down'] = False
        print(Fore.RED + 'pencil_down released' + Style.RESET_ALL)

    if drawing_data['pencil_down'] == True:
        # cv2.circle(image_rgb, (x, y), 3, (255,255,255), -1)
        cv2.line(image_rgb, (drawing_data['previous_x'], drawing_data['previous_y']), (x,y), drawing_data['color'], 1) 

    drawing_data['previous_x'] = x
    drawing_data['previous_y'] = y




def main():

    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    capture = cv2.VideoCapture(4)
    window_name = 'window'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    while True:
        _, image = capture.read()  # get an image from the camera


        # -----------------------------------------------
        # Visualization 
        # -----------------------------------------------
        cv2.imshow(window_name, image)
        cv2.waitKey(25)

    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------

if __name__ == '__main__':
    main()