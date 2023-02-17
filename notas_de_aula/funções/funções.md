# Funções

São ferramentas para que seja possível reorganizar o código idealmente tornando ele mais modular e conciso.

```python
def nome_função():
    """
    Docstring que é um comentário que explica o que a função faz
    Nesse caso a função imprime 'Hello' e depois 'oi'
    """
    print("Hello")
    print("Oi")

# Para chamar (fazer com que ela execute o código) uma função
# devemos escrever o identificador com abre e fecha parenteses depois.
nome_função()
# Executa a mesma função de novo
nome_função()
```

## Nomenclatura

dado o código:

```python
def identificador(parâmetro1, parâmetro2, parâmetro3):
    # Bloco de comandos
```

`def` é uma palavra reservada de Python para identificar que o que vem a seguir é uma definição de uma função.
As variáveis `parâmetro1`, `parâmetro2`, `parâmetro3` são os parâmetros de uma função.

Quando chamamos uma função com `identificador(1, 2, 3)` nesse caso os valores `1`, `2` e `3` são os argumentos da função.

```python
def função1(par1, par2, par3):
    print(par1)
    print(par2)
    print(par3)
print("Incio do Programa")
```

Definir uma função não executa essa função.

Para executar uma função ela deve ser _chamada_.
_Chamar_ uma função é passar os argumentos para ela entre os parênteses.

```python
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
```

O código acima pode ser encontrado [aqui](stack.py).

O que você espera que seja impresso no console?

```python
def soma(a, b, c):
    return a + b + c


resultado = soma(3, 4, 5)
print(resultado)
print(soma(-1, 1, 0))
```

Uma função pode retornar um valor usando a palavra `return`.
Quando a instrução return é encontrada o valor será retornado para a função que chamou e o restante da função é abortado.

# Recursão

Uma função pode chamar ela própria para resolver algum problema.
Essa técnica é chamada de recursão.

No código abaixo, que pode ser encontrado [aqui](fatorial.py), a palavra `raise` pode ser interpretada como um "`return`" diferente.
Ela gera um tipo de erro que deve ser tratado de uma forma especial, ou o programa simplesmente para de funcionar, teste chamar a função com um número negativo.

```python
def fatorial(n):
    if n < 0:
        raise TypeError("n não pode ser negativo")
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

A pilha de chamadas de funções em python não pode ultrapassar `1000` chamadas, portanto, a recursão só deve ser usada com parcimônia sabendo dessas limitações.

Toda função recursiva pode ser convertida em uma não recursiva.

```python
def Fibonacci(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    return Fibonacci(i-1) + Fibonacci(i - 2)
```

## Argumentos nomeados

Função para imprimir `3` strings usando como separador um parâmetro opcional.

```python
def imprime_tudo(stringA, stringB, stringC, sep="+"):
    resultado = sep.join([stringA, stringB, stringC])
    return resultado

print(imprime_tudo("A", "B", "C", "++")) # Quando chamada com um quarto argumento ela vai usar ele para separar as strings
print(imprime_tudo("A", "B", "C")) # Se o quarto parâmetro é omitido o padrão "+" vai ser usado
print(imprime_tudo("A", "B", "C", sep="-")) # Podemos também usar o nome do quarto parâmetro para passar um argumento para ele
```

Também podemos usar os nomes dos parâmetro para mudar a ordem dos argumentos.

```python
def é_tri_retângulo(cateto1, cateto2, hipotenusa):
    if cateto1**2 + cateto2**2 == hipotenusa**2:
        return True
    return False

lado1 = 3
lado2 = 4
lado3 = 5

print(é_tri_retângulo(3, 4, 5))
print(é_tri_retângulo(5, 4, 3))

print(é_tri_retângulo(hipotenusa=5, cateto1=3, cateto2=4)) # Podemos chamar invertendo a ordem que isso não é problema, contanto que usemos os nomes corretamente
```

## O Escopo das variáveis

Toda variável em Python ao executar uma instrução vai ser _alvo_ ou _fonte_.

- **Alvo**: quando a variável vai receber um valor novo.
- **Fonte**: quando o conteúdo da variável vai ser usado para alguma coisa.

Na instrução, `x = 10` a variável `x` é _alvo_.
Na instrução, `x = x + 10` a variável `x` é tanto _alvo_ quanto _fonte_.

O _escopo_ de uma variável é a definição de qual parte do código pode usar uma variável como _alvo_ ou _fonte_.
Na linguagem Python, o escopo das variáveis é o bloco da função que aonde a variável é declarada.

```python
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
```

Tem valores que são imutáveis, isso quer dizer que não tem como mudar, sem fazer de forma explicita, um valor passado como argumento de uma função, na variável de fora dessa função.
Como exemplo, considere a execução do código abaixo.

```python
def soma_10(i):
    print(f'Dentro - O valor de i antes {i}')
    i += 10
    print(f'Dentro - O valor de i depois {i}')


i = 20
print(f'Fora - O valor de i antes {i}')
soma_10(i)
print(f'Fora - O valor de i depois {i}')
```

## Leitura Recomendada

Leia o restante do capítulo [Functions](https://automatetheboringstuff.com/2e/chapter3/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter3/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter3/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
