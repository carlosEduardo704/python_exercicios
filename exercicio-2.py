"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""

from random import randint

valores = [randint(1, 100) for i in range(6)]

print(f'Os valores são: {valores}')

for valor in valores:
    print(valor)
