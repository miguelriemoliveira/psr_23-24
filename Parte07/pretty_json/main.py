#!/usr/bin/env python3 
import argparse
import json
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style


def main():

    d = {'limits': {'B': {'max': 255, 'min': 0},
            'G': {'max': 255, 'min': 0},
            'R': {'max': 255, 'min': 229}}}
  
    print(d)

    d_formatted = json.dumps(d, indent=2)

    print(d_formatted)


if __name__ == '__main__':
    main()