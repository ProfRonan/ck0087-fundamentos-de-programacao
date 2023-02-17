def lista_quadrada(lista):
    """
    Pega cada elemento da lista passada como argumento e faz ele virar o quadrado dele mesmo.
    """
    for i in range(len(lista)):
        lista[i] *= i


lista_teste = [1, 2, 3, 4, 5]
lista_quadrada(lista_teste)
print(lista_teste)
