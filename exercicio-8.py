"""
Crie um programa que leia 6 valores inteiros e, em seguida, imprima
os valores em ordem inversa.

"""

from random import randint as R


valores = [R(1, 10000) for i in range(6)]

print(valores)
print(valores[::-1])
