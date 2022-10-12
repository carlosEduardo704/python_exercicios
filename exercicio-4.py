"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também
dois valores 'x' e 'y' quaisquer correspondentes a duas posições do vetor.
Ao final su programa devera escrever a soma dos valores encontrados nas respectivas
posições 'x' e 'y'.

"""

from random import randint as R

vetor = [R(1, 100) for valor in range(8)] # 'R' é o randint.

x = vetor[R(0, 7)]
y = vetor[R(0, 7)]

soma = x + y

print(f" O valor de 'x' é: {x}\n O valor de 'y' é: {y}")
print(f' A soma de x + y é: {soma}')