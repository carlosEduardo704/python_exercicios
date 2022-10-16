"""
Faça um programa que preencha um vetor com 10 numeros reais, calcule e mostre a
quantidade de números negativos e a soma dos numeros positivos.

"""
from random import randint as R


vetor = [R(-1000, 1000) for i in range(10)]

def soma_positivos(x):
    soma = 0
    for valor in x:
        if valor > 0:
            soma += valor
    return soma


def quantidade_negarivos(x):
    quantidade = 0
    for valor in x:
        if valor < 0:
            quantidade += 1
    return quantidade


print(f'O vetor é: {vetor}\n'
      f'A quantidade de números negativos é: {quantidade_negarivos(vetor)}\n'
      f'A soma dos números positivos é: {soma_positivos(vetor)}'

)