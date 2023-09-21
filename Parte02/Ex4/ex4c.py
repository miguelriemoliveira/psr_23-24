#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, September 2023.
# --------------------------------------------------

import argparse

import readchar

# Use imports here
from colorama import Fore, Back, Style

# Define functions here ...

# maximum_number = 30

def  countNumbersUpto(stop_char):

    print('Start typing')

    keys =[]
    while True:
        key = readchar.readkey()
        keys.append(key)
        print('You typed ' + key)

        if key == stop_char:
            break

    print(keys)

    n_numeric = 0
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
        
    print('You pressed on ' + str(n_numeric) + ' numeric keys')

def main():
    countNumbersUpto('x')


if __name__ == "__main__":
    main()