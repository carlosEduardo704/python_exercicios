"""

"""

from random import randint as Rd

vetor = [Rd(1, 50) for i in range(50)]

vetor_impares = [valor for valor in vetor if valor % 2 != 0]

print(vetor_impares)