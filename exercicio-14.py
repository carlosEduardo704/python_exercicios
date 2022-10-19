"""
Faça um progama que leia um vetor de 10 posições e verifique se existem valores iguais
e os escreva na tela.
"""

from random import randint as Rd

vetor = [Rd(1, 20) for i in range(10)]

valores_repetidos = {}

for valor in vetor:
    repeticoes = 0
    for comparacao in vetor: # Se os valores comparadas forem iguais a variável repeticoes recebe +1.
        if comparacao == valor:
            repeticoes += 1
    if repeticoes > 1:
        valores_repetidos[valor] = repeticoes # Se o valor tiver alguma repetição é adiconado ao dicionário.



print(
    f'Os valores são: {vetor}\n'
    f'Os valores repetidos são: {valores_repetidos}'
)