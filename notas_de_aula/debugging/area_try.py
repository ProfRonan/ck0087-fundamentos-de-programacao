def area(lado):
    tipos = [int, float]
    if type(lado) not in tipos:
        raise TypeError("lado tem que ser int ou float")
    if lado < 0:
        raise ValueError("lado tem que ser maior ou igual à zero")
    return lado * lado


lado = input("Digite o lado do quadrado que deseja calcular a área: ")
try:
    lado = float(lado)
except ValueError:
    print("Você digitou um valor que não é um número.")
    exit()

try:
    area_quadrado = area(lado)
except TypeError:
    print("area só pode ser calculado com um valor numérico")
    exit()
except ValueError:
    print("o lado de um quadrado não pode ser negativo")
    exit()
except Exception:
    print("algum outro erro desconhecido aconteceu.")
    exit()
else:
    print(f"A área do quadrado é {area_quadrado}")
