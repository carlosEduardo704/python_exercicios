


from random import randint as R

notas = [R(15, 100) for i in range(15)]

media = sum(notas) / len(notas)
print(media)