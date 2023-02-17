a = "Primeira"
b = "Primeira"
c = a
print(id(a))  # id(variável) diz qual a posição de memória dessa variável.
print(id(b))
# Como as duas strings são idênticas, o interpretador faz uma otimização e coloca elas no mesmo lugar.
print(id(b) == id(a))

print(id(c))
# como são a mesma string o resultado é que elas ficam no mesmo lugar da memória.
print(id(c) == id(a))
