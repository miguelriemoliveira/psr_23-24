#!/usr/bin/env python3 
import argparse
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style


def main():

    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    capture = cv2.VideoCapture(1)
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