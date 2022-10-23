"""
Faça um programa que receba dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denomidado C calculando A - B. Mostre na tela os dados do vetor C.
"""

from random import randint as rd

# Vetores
A = [rd(1, 100) for i in range(10)]
B = [rd(1, 100) for j in range(10)]

C = set(A) - set(B)

print(f'O vetor C é : {list(C)}')
