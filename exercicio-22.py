"""
Faça um programa que leia dois vetores de 10 posições e calcule outro
vetor contento nas posições pares os valores do primeiro vetor e nas
posições ímpares os valores do segundo vetor.
"""

from random import randint as rd

vetor_A = [rd(1, 100) for i in range(10)]

vetor_B = [rd(1, 100) for j in range(10)]

vetor_C = []

while len(vetor_C) < 10:
    if len(vetor_C) % 2 == 0:
        vetor_C.append(vetor_A[len(vetor_C)])
    else:
        vetor_C.append(vetor_B[len(vetor_C)])

print(f'O primeiro vetor é: {vetor_A}\n'
      f'O segundo vetor é: {vetor_B}\n'
      f'O terceiro vetor é: {vetor_C}')
