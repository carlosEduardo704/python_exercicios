"""
Faça um vetor de tamanho 50 preenchido com o seguuinte valor (i + 5*i) % (i + 1), sendo
i a posição do elemento no vetor. Em seguida imprima o vetor na tela.
"""

from random import randint as Rd

vetor = [(i + 5*i)%(i + 1) for i in range(50)]

print(vetor)