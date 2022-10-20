"""
Leia um vetor de 10 posições e atribua o valor 0 para todos os elementos que
possuírem valores negativos.
"""

from random import randint as Rd

vetor = [Rd(-10, 10) for i in range(10)]

vetor_substituido = [0 if valor < 0 else valor for valor in vetor]


print(vetor, vetor_substituido)