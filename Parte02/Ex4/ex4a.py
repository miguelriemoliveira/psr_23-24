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

def printAllCharsUpTo():

    # Passo 1: ler um carater do terminal -> readchar 
    print('Press a key to read a char ')
    key = readchar.readkey()
    print('User pressed ' + key)

    # Passo 2: lido -> char? calcular o númeor correspondente ao lido  chr ou ord
    number = ord(key)
    print('Corresponding number is ' + str(number))

    # passo 3: percorrer todos os numeros deste o espaço (32) até ao nmero lido, 
    # e para cada iteração imprimir o carater correspondente

#     for i in range(32,number):
#         print(chr(i), end='')
 
    chars_to_print = []
    for i in range(32,number):
        chars_to_print.append(chr(i))
 
    print(''.join(chars_to_print))



def main():

    printAllCharsUpTo()


if __name__ == "__main__":
    main()