from random import randint

def cria_lista(x: int, y: int, z: int):
    vetor = [randint(x, y) for i in range(z)]
    return vetor