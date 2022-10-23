"""
Escreva um programa que leia números inteiros no intervalo de [0, 50] e os armazene em um vetor
com 10 posições. Preencha um segundo vetor apenas com os númeres ímpares do primeiro vetor. 
"""

from random import randint as Rd

vetor = [Rd(1, 50) for i in range(10)]

vetor_impares = [valor for valor in vetor if valor % 2 != 0]

print(
    f'O vetor é: {vetor}\n'
    f'O vetor com os números impares é : {vetor_impares}'
)