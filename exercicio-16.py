"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um
código inteiro. Se o código for zero, finalize o programa;se for 1, mostre o vetor
na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente
de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""

from random import randint as Rd

vetor = [Rd(1, 100) for i in range(5)]

print(vetor)

while True:
    escolha = input(
        '======================================\n'
        '|        Escolha uma opção!          |\n'
        '======================================\n'
        '======================================\n'
        '| 1 - Mostrar Vetor na Ordem Normal  |\n'
        '======================================\n'
        '======================================\n'
        '| 2 - Mostrar Vetor na Ordem Inversa |\n'
        '======================================\n'
        ':'
    )

    if escolha == '1':
        print(
        '======================================\n'
        f'|        {vetor}         |\n'
        '======================================\n'
        )
        break
    elif escolha == '2':
        print(
        '=======================================\n'
        f'|        {vetor[::-1]}         |\n'
        '=======================================\n'
        )
        break
    else:
        print('Valor inválido!')
        break