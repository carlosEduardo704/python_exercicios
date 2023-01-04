"""
Faça um programa que leia um vetor de 10 números. Leia um número X. Conte os
múltiplos de um número inteiro X num vetor e mostre-os na tela.
"""

from random import randint as Rd

escolha = int(input(
    'Digite um número para encontrar os múltiplos!\n'
    f'{"-" * 50}\n'
    'Digite 0 para sair!\n'
    f'{"-" * 50}\n'
    ': '
))

try:
    if escolha == 0:
        print('Ok, até logo!')
    else:
        vetor = [Rd(1, 100) for i in range(10)]

        multiplos = [valor for valor in vetor if valor % escolha == 0]

        print(
            f'Os números são: {vetor}\n'
            f'Os múltiplos do número {escolha} são: {multiplos}')

except:
    print('Valor inválido!')
