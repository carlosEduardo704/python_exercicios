"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar
entre eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o produto escalar,
sendo que o produto escalar é dado por: X1 * Y1 + X2 * Y2 + ... + Xn * Yn.
"""

from random import randint as rd

vetor1 = [rd(1, 1000) for i in range(5)]

vetor2 = [rd(1, 1000) for j in range(5)]

produto_escalar = 0

for i in range(len(vetor1)):
    produto_escalar += vetor1[i] * vetor2[i]


print(f'O primeiro vetor é: {vetor1}\n'
      f'O segundo vetor é: {vetor2}\n'
      f'O produto escalar é: {produto_escalar}')
