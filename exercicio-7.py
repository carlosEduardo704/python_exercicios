"""
Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.

"""

from random import randint as R

vetor = [R(1, 5000) for numero in range(10)]

print(f'O vetor é: {vetor}\n'
      f'O maior elemento do vetor é: {max(vetor)}\n'
      f'A posição do maior elemento do vetor é: {vetor.index(max(vetor))}'
)
