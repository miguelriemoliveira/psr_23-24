#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, September 2023.
# --------------------------------------------------

import argparse
from collections import namedtuple

import readchar

# Use imports here
from colorama import Fore, Back, Style


def main():

    # Variáveis soltas
    nome1 = 'Gustavo'
    nacionalidade1 = 'Brasil'
    altura1 = 1.75
    peso1 = 50

    nome2 = 'Miguel'
    nacionalidade2 = 'Portugal'
    altura2 = 1.95
    peso2 = 50

    peso1 += 5

    # N Listas
    nomes = ['Gustavo', 'Miguel']
    nacionalidades = ['Brasil', 'Portugal',]
    alturas = [1.75, 1.95]
    pesos = [50,50]

    pesos[0] = pesos[0] + 5

    # 1 Lista de tuplos
    pessoas = [('Gustavo', 'Brasil', 1.75, 50) ,
               ('Miguel', 'Portugal', 1.95, 50)]

    # pessoas[0][3] = pessoas[0][3] + 5
    print(pessoas[0][1])

    # 1 Lista de named tuples
    Pessoa = namedtuple('Pessoa', ['nome', 'nacionalidade',  'altura', 'peso'])

    pessoas = [Pessoa('Gustavo', 'Brasil', 1.75, 50) ,
               Pessoa('Miguel', 'Portugal', 1.95, 50)]

    print(pessoas[1].altura)

    # 1 dicionarios nested
    pessoas = {'Gustavo': {'nacionalidade': 'Brasil', 'altura': 1.75, 'peso': 50}, 
               'Miguel': {'nacionalidade': 'Portugal', 'altura': 1.95, 'peso': 50} }

    print(pessoas)
    pessoas['Gustavo']['peso'] = pessoas['Gustavo']['peso']  + 5
    print(pessoas['Gustavo']['nacionalidade'])

    # Engordar
    def engordar(pessoa):
        pessoa['peso'] = pessoa['peso'] + 5
        return pessoa

    pessoas['Gustavo'] = engordar(pessoas['Gustavo'])

    print(pessoas['Gustavo']['peso'])

    class Pessoa:

        def __init__(self, nome, nacionalidade, altura, peso):
            self.nome = nome            
            self.nacionalidade = nacionalidade            
            self.altura = altura
            self.peso = peso

        def engordar(self, extra):
            self.peso += extra

        def __str__(self):
            return 'Nome: ' +self.nome + ', Nacionalidade: ' + self.nacionalidade + ', altura ' +  str(self.altura) + ' ,peso ' + str(self.peso)

        def __repr__(self):
            return self.__str__()


    p = Pessoa('Goncalo', 'Brasil', 1.75, 50)
    a = int(5)

#     pessoas = [Pessoa('Gustavo', 'Brasil', 1.75, 50),
#                Pessoa('Miguel', 'Portugal', 1.95, 50),]
#     
#     
#     print(pessoas)
# 
#     pessoas[0].engordar(25)
#     print(pessoas[0])


if __name__ == "__main__":
    main()