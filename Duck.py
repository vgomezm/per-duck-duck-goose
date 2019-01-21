import random
lista=["Nacho", "Andrea", "Tania", "Vanesa"]
posicion=random.randrange(int(len(lista)))


def pato (lista, posicion):

    return(lista[posicion])

resultado=pato(lista, posicion)
print(resultado)
