"""
Leia um vetor de 10 posições. Contar e escrever quantos
valores pares ele possui.

"""

from random import randint as R


vetor = [R(1, 1000) for valor in range(10)]
vetor_pares = []

for valor in vetor:
    if valor % 2 == 0:
        vetor_pares.append(valor)

print(f'Os valores do vetor são: {vetor}\n'
      f'A quantidade de valores pares é: {len(vetor_pares)}\n'
      f'Os valores pares são: {vetor_pares}')