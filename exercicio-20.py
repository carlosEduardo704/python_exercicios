"""
Escreva um programa que leia números inteiros no intervalo de [0, 50] e os armazene em um vetor
com 10 posições. Preencha um segundo vetor apenas com os númeres ímpares do primeiro vetor. 
"""

from random import randint as Rd

vetor = [Rd(1, 50) for i in range(50)]

vetor_impares = [valor for valor in vetor if valor % 2 != 0]

print(vetor_impares)