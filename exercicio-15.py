"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando
elementos repetidos.
"""

from random import randint as Rd

vetor = [Rd(1, 20) for  i in range(20)]

# Forma - 1
vetor_sem_repetidos = []

for valor in vetor:
    repeticao = -1
    for comparacao in vetor:
        if valor == comparacao:
            repeticao += 1
    if repeticao == 0:
        vetor_sem_repetidos.append(valor)

print(vetor)
print(vetor_sem_repetidos)

# Forma 2

from collections import Counter

contagem = dict(Counter(vetor))
vetor_sem_repetidos = []

for chave, valor in contagem.items():
    if valor == 1:
        vetor_sem_repetidos.append(chave)

print(vetor_sem_repetidos)