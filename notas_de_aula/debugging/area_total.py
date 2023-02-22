def area(lado):
    tipos = [int, float]
    if type(lado) not in tipos:
        raise TypeError("lado tem que ser int ou float")
    if lado < 0:
        raise TypeError("lado tem que ser maior ou igual à zero")
    return lado * lado


lado = input("Digite o lado do quadrado que deseja calcular a área: ")
lado = float(lado)
area_quadrado = area(lado)

print(f"A área do quadrado é {area_quadrado}")
