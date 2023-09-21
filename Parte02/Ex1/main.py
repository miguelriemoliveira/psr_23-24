#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, September 2023.
# --------------------------------------------------

# Use imports here
from colorama import Fore, Back, Style

# Define functions here ...

maximum_number = 500

def getDividers(value):
    """Gets a list of integer dividers of number value

    Args:
        value: number to get dividers.

    Returns:
        bool: is perfect (True) or not (False)
    """


    # create an empty list
    dividers = []

    for i in range(1,value):
        if value%i == 0: # its an integer divider
            dividers.append(i) # add this divider to the list of dividers

    return dividers

def isPerfect(value):

    dividers = getDividers(value)

    return value == sum(dividers)


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

        # dividers = getDividers(i)
        # print('Number ' + str(i) + ' has dividers ' +str(dividers))


if __name__ == "__main__":
    main()