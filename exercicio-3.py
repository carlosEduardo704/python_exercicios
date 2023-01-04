"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
dos componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos
tem 10 elementos cada. Imprimir todos os conjuntos.
"""

from random import randint


numeros = [randint(1, 100) for numero in range(10)]

numeros_ao_quadrado = [numero**2 for numero in numeros]

print(f'Os numeros são: {numeros}')
print(f'Os números ao quadrado são: {numeros_ao_quadrado}')
