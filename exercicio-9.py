"""
Crie um programa que leia 6 valores inteiros pares e, em seguida, imprima
os valores em ordem inversa.

"""

from random import randint as R


valores = []

while len(valores) < 6:
    valor = R(1, 3000)
    if valor % 2 == 0:
        valores.append(valor)
    else:
        pass

print(valores)

print(valores[::-1])