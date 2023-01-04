"""
Faça um programa que leia dois vetores de 10 elementos cada.
Crie um vetor que seja a união entre os dois vetores anteriores, ou seja,
que contenha os valores de ambos os vetores. Não deve conter números repetidos.
"""

from random import randint as rd

vetor_a = [rd(1, 50) for i in range(10)]

vetor_b = [rd(1, 50) for i in range(10)]

vetor_uniao = []

for i in range(10):
    vetor_uniao.append(vetor_a[i])
    vetor_uniao.append(vetor_b[i])

print(f'{vetor_a}\n{vetor_b}')
print(list(set(vetor_uniao)))
