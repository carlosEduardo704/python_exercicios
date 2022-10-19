"""
Faça um programa que leia 5 valores e imprima a posição do maior e do menor valor.
"""

from funcoes import cria_lista

valores = cria_lista(1, 1000, 5)


print(
    f'Os valores são: {valores}\n'
    f'O maior valor está na posição: {valores.index(max(valores))}\n'
    f'O menor valor está na posição: {valores.index(min(valores))}'
)
