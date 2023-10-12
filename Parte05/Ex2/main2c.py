#!/usr/bin/env python3 
import argparse

import cv2


def main():

    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

    args = vars(parser.parse_args()) # creates a dictionary
    print(args)


    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    
    image_b, image_g, image_r = cv2.split(image_rgb) 

    retval, image_b_thresholded = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    retval, image_g_thresholded = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    retval, image_r_thresholded = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)


    image_rgb_thresholded = cv2.merge([image_b_thresholded, image_g_thresholded, image_r_thresholded]) 

    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_rgb_thresholded', image_rgb_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()