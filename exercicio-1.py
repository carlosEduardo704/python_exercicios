"""
Faça um programa que possua um vetor denominado 'a' que armazene 6 números inteiros.
O programa deve executar os seguintes passos:

(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores da posições
    A[0], A[1], A[5] do vetor e mostre na tela a soma.
(c) Modifique o vetor na possição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""

a = [1, 0, 5, -2, -5, 7]

soma = a[0] + a[1] + a[5]

print(f'A soma é: {soma}')

a[4] = 100

for valor in a:
    print(valor)