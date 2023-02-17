# Programa para mostrar um cumprimento na tela ao usuário

print("Oi, tudo bem?")
print("Qual o seu nome?")
nome = input()  # pergunta o nome
print("Prazer em te conhecer, " + nome)
print("O tamanho do seu nome é")
print(len(nome))  # len é uma função que resulta no tamanho do item passado para ela
print("Qual a sua idade?")
idade = input()  # pergunta a idade
print("Ano que vem você terá " + str(int(idade) + 1) + " anos")
