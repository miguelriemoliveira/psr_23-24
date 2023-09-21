#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style

# define functions here ...

maximum_number = 500

def getDividers(value):
    # create an empty list
    dividers = []

    for i in range(1,value):
        if value%i == 0: # its an integer divider
            dividers.append(i) # add this divider to the list of dividers

    return dividers

def isPerfect(value):

    dividers = getDividers(value)

    return value == sum(dividers)

# def isPerfect(value):
#     
#     # Percorrer todos os numeros até ao número em análise
#     # para cada umero, ver se é um divisor inteiro
#     # Se for, somar num acumulador
#     accumulator = 0
#     for i in range(1, value):
#         if value%i == 0: # its an integer divider
#             accumulator = accumulator + i
# 
#     # Ver se a soma dos dividores inteiros é igual ao próprio número
#     return accumulator == value

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

        # dividers = getDividers(i)
        # print('Number ' + str(i) + ' has dividers ' +str(dividers))


if __name__ == "__main__":
    main()