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

    # Ex5b
    numerical_keys = []
    for key in keys:
        if key.isnumeric():
            numerical_keys.append(key)


    print('Numerical keys' + str(numerical_keys))

    # Ex5c 
    #['a', '1', 'b', '2', 'c', '3', 'd', '4', 'x']

    # {0, 'a', 1: '1', 2: 'b', ...}
    d_keys = {}
    for key_idx, key in enumerate(keys):
        d_keys[key_idx] = key

    print('d_keys = ' + str(d_keys))

    # Ex 5d
    numerical_keys.sort()
    print('Numerical keys' + str(numerical_keys))

    #Ex e) 

    # List comprehension
    numerical_keys2 = [x for x in keys if x.isnumeric()]
    print('Numerical keys2' + str(numerical_keys2))

    d_keys2 = {idx:x for idx,x in enumerate(keys)}
    print('d_keys2 ' + str(d_keys2))


    

def main():
    countNumbersUpto('x')


if __name__ == "__main__":
    main()