"""
Faça um programa que lê a nota da prova de 15 alunos e as amazene em um vetor,
calcule e imprima a média geral.
"""


from random import randint as R

notas = [R(15, 100) for i in range(15)]

media = sum(notas) / len(notas)

print(f'A media geral é: {media:.2f}')
