"""
Faça um programa que receba 6 números inteiros e mostre:
    Os números pares;
    A soma dos números pares digitados;
    Os números impares;
    A quantidade de números ímpares;
"""

# Imports
from random import randint as rd

vetor = [rd(1, 1000) for i in range(6)]


def par_ou_impar(i: int):
    """Retorna True se número par, se for ímpar, retorna False"""
    if i % 2 == 0:
        return True
    else:
        return False


pares = [num for num in vetor if par_ou_impar(num)]

impares = [num for num in vetor if par_ou_impar(num) is False]

print(f'O vetor é: {vetor}\n'
      f'Os números pares: {pares}\n'
      f'A soma dos números pares: {sum(pares)}\n'
      f'Os números ímpares: {impares}\n'
      f'A quantidade de números ímpares: {len(impares)}')
