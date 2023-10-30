#!/usr/bin/env python3 
import argparse
import json
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style

global_result = 77
g_a = 22

def somar(b, a):

    # global global_result
    # global_result = a + b
    return a + b

def subtract(subtrator):
    global g_a
    return g_a - subtrator

def main():
    global global_result, g_a

    a = 3.0
    b = 7.0

    # c = somar(a,b)
    # print(c)

    global_result = global_result + 1
    # c = somar(a,b)
    print(global_result)

    d = subtract(4)
    print(d)

if __name__ == '__main__':
    main()