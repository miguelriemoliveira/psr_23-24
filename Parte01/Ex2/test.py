#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style

# define functions here ...

maximum_number = 10

def isPrime(value):
    for i in range(2,value):
        if value%i == 0:
            # print('the number ' + str(value) + ' is not prime because we divide by ' + str(i))
            return False

    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number): # for cycle to go from o to 10
        if isPrime(i):
            print('Number ' + Back.YELLOW + Fore.BLUE + str(i) + Style.RESET_ALL + ' is prime.' )
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()