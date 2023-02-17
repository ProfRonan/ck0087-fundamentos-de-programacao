# O resultado de input é convertido em inteiro e isso é armazenado na idade
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Não tem como você não ter nascido ainda!")
elif idade < 3:
    print("Você é um bebê")
elif idade < 10:
    print("Você é uma criança")
elif idade < 18:
    print("Você é um adolescente")
elif idade < 25:
    print("Você é um jovem!")
else:
    print("Vá pra casa vovô!")
