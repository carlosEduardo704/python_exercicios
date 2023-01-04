"""
Crie um programa que receba do usuário um vetor de 10 posições. Em seguida deverá ser
impresso o maior e o menor valor do vetor.

"""

from random import randint as R

vetor = [R(1, 1000) for i in range(10)]

print(f'O vetor é {vetor}\n'
      f'O maior valor é: {max(vetor)}\n'
      f'O menor valor é: {min(vetor)}')
