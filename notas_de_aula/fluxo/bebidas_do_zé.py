# Sistema de venda de bebidas alcoólicas

print("Bem vindo ao depósito de bebidas do seu Zé.")
print("Qual a sua idade?")
idade = input()
idade = int(idade)  # Converte a idade logo para inteiro

if idade > 18:
    print("Compre a vontade")
else:
    print("Você é muito novo para comprar")
