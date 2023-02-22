def ordena(lista):
    """
    Ordena uma lista passada como argumento na ordem crescente ou lexicográfica
    """
    for índice, _ in enumerate(lista):
        if lista[índice] > lista[índice + 1]:
            lista[índice], lista[índice + 1] = lista[índice + 1], lista[índice]


lista = [3, 2, 1]

ordena(lista)

print(lista)
