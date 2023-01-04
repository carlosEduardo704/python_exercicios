"""
Faça um programa que leia dois vetores de 10 elementos cada.
Crie um vetor que seja a interseção entre os dois vetores anteriores, ou seja,
que contenha apenas os valores que estão em ambos os vetores. Não deve conter números repetidos.
"""

from random import randint as rd

vetor_a = [rd(1, 10) for i in range(10)]

vetor_b = [rd(1, 10) for j in range(10)]

vetor_interseccao = []

for valor in vetor_a:
    if valor in vetor_b:
        vetor_interseccao.append(valor)


print(vetor_a, vetor_b)
print(list(set(vetor_interseccao)))
