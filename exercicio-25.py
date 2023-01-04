"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais
que não são múltiplos de 7 ou que terminam com 7.
"""


def verifica_multiplo(num: int):
    """ verifica se o número é divisível por 7 """
    """  Caso o resto da divisão de num por 7, for diferente de 0, retorna False"""
    try:
        if num % 7 != 0:
            return False
        else:
            return True
    except ValueError:
        return False


def termina_em_sete(num: int):
    """ Verifica se o número termina em 7 """
    try:
        if num != 0 and str(num)[-1] != '7':  # Retorna False caso não seja um número, seja 0 ou termine com 7.
            return True
        else:
            return False
    except ValueError:
        return False


vetor = []

numero = 0

while len(vetor) < 100:
    if termina_em_sete(numero) and verifica_multiplo(numero):  # Se termina_em_sete for False e numero ser multiplo de 7
        vetor.append(numero)  # adicionamos o número no vetor
    else:
        pass  # Caso não seja, passamos para o próximo número.
    numero += 1

print(vetor)
