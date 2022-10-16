"""
Faça um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores.
"""

from random import randint as R

valores = [R(1, 1000) for i in range(5)]

print(
    f'Os valores são: {valores}\n'
    f'O maior valor é: {max(valores)}\n'
    f'A média dos valores é: {sum(valores) / len(valores):.2f}'
)
