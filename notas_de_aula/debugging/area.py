def area(lado):
    tipos = [int, float]
    if type(lado) not in tipos:
        raise TypeError("lado tem que ser int ou float")
    if lado < 0:
        raise TypeError("lado tem que ser maior ou igual à zero")
    return lado * lado
