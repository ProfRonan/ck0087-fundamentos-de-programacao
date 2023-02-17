def a():
    print("Inicio de A")
    b()
    print("Fim de A")


def b():
    print("Início de B")
    c()
    print("Fim de B")


def c():
    print("Rodou C")


a()  # Aqui se faz a chamada de a
print("Fim do Programa.")
