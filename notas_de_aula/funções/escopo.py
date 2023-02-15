# As variáveis x, y, z aqui fazem parte do módulo e não estão dentro de nenhuma função
x = 1
y = 2
z = 3
# Variáveis que fazem parte de um módulo podem tem podem ser fonte em todo o módulo e funções internas dele.


def funA():
    # Aqui as variáveis x, y, z estão como alvo das instruções
    # Como x, y, z do módulo não podem ser alvo, o interpretador cria novas variáveis x, y, z que tem como escopo (alvo e fonte) a função funA e todos os blocos mais internos.
    x = "A1"
    y = "A2"
    z = "A3"
    print("Depois de mudar")
    print(x, y, z)


print("Antes de executar A")
# Como aqui está fora do escopo de funA, as variáveis x, y, z usadas como fonte são as primeiras declaradas.
print(x, y, z)
funA()
print("Fora da função depois de executar")
print(x, y, z)
