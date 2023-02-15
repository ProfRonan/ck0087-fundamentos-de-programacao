# Controle de Fluxo

Existem construções nas linguagens de programação que permitem controlar quais partes do código devem ser executadas.

# Estrutura de Decisão

Um _estrutura de decisão_ é uma ferramenta de uma linguagem de programação que permite executar uma parte do código ou outra a depender de uma **condição** ser verdadeira ou falsa.

```python
# Sistema de venda de bebidas alcoólicas

print("Bem vindo ao depósito de bebidas do seu Zé.")
print("Qual a sua idade?")
idade = input()
idade = int(idade) # Converte a idade logo para inteiro

if idade > 17: # A condição é verdadeira se o valor guardado em idade for maior que 17
  print("Compre a vontade")
else:
  print("Você é muito novo para comprar")
```

Temos somente uma estrutura de decisão em python o comando `if/elif/.../elif/else`.

## Booleanos

São um tipo de dados que só podem assumir dois valores `True` ou `False`.

```python
>>> condição = True
>>> if condição:
>>>     print("A condição é verdadeira")
'A condição é verdadeira'
>>> condição_falsa = False
>>> if condição_falsa:
>>>     print("A condição é verdadeira")
>>> print("Qualquer coisa")
'Qualquer coisa'
```

> Quando o comando `if` testa uma condição e o resultado dela é `True` ele executa todo o _bloco de comandos_.
>
> Quando o `if` testa uma condição e o resultado dela é `False` o _bloco de comandos_ é pulado.

## Comparações

Os comparadores mais comuns em Python são:

- Igualdade `==`
- Diferente `!=`
- Menor que `<`
- Maior que `>`
- Menor ou igual à `<=`
- Maior ou igual à `>=`

```python
>>> 42 == 42
True
>>> 42 == 43
False
>>> 42 != 43
True
>>> 2 + 2 >= 4
True
>>> 2 + 2 == 4
True
>>> 2 ** 10 < 10 ** 2
False
```

Também podemos comparar strings:

```python
>>> "a" < "b"
True
>>> "A" < "a"
True
>>> "abacaxi" == "banana"
False
>>> "abacaxi" > "banana"
False
```

Ou os próprios Booleanos:

```python
>>> True == True
True
>>> False == False
True
>>> False < True # O que!?!?
True
```

E podemos misturar

```python
>>> "42" == 42 # String e números são coisas diferentes
False
>>> True == 1 # Agora vamos complicar...
True
>>> False == 0
True
>>> False + False
0
>>> False + False + True + True
2
```

## Operações Booleanas

Uma expressão booleana é uma expressão que pode ser avaliada em `True` ou `False`, mas não ambas.

### `and`

O operador booleano `and` recebe duas expressões booleanas e o resultado é `True` se e somente se as duas são verdadeiras.

```python
>>> (2 == 2) and (3 < 4)
True
>>> (2 != 2) and (3 < 4)
False
```

### `or`

O operador booleano `or` recebe duas expressões booleanas e o resultado é `True` se pelo menos uma é verdadeira.

```python
>>> (2 == 2) or (3 < 4)
True
>>> (2 != 2) or (3 < 4)
True
```

### `not`

O operador booleano `not` recebe uma expressão booleana e o resultado é o inverso da expressão original.

```python
>>> not True
False
>>> not False
True
>>> not (2 == 2)
False
>>> not (3 > 4)
True
```

## O commando `if/elif/.../elif/else`

Na sua forma mais simples o comando `if` e da seguinte forma:

```python
nome = "João"
if nome == "João":
    print("Bem vindo João")
    print("Como posso ajudá-lo?")
```

O `if` é sempre seguido de uma expressão booleana, ou algo que possa ser convertido em uma expressão booleana, seguido de dois pontos e depois um bloco de commandos.

> Um bloco de comandos é uma sequencia de um ou mais comandos que tem um recuo (quantidade de espaço em branco) maior que o bloco anterior.

O `if` também pode ser seguido do seu complemento opcional `else` seguido de dois pontos e um outro bloco de comandos que será executado quando a condição não for verdadeira.

```python
nome = input("Digite o nome de usuário: ")
if nome == "João":
    print("Bem vindo João")
else:
    print("Bem vindo usuário desconhecido.")
```

> Blocos de comandos podem conter mais blocos de comandos
>
> ```python
> nome = input("Digite seu nome: ")
> if nome == "Zé":
>     print("Bem vindo zé!")
>     senha = input("Digite sua senha: ")
>     if senha == "123456":
>         print("Você acertou a senha!")
>     else:
>         print("você errou a senha")
> else:
>     print("Só aceito o usuário com nome Zé!")
> ```

Finalmente, entre o if e o else também podemos ter opcionalmente pelo menos um comando `elif` cada um deles seguido de uma condição e um bloco de comandos que será executado quando a condição for verdadeira

```python
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
```

O arquivo [idade.py](idades.py) contem o código acima.
Experimente trocar os `elif`s por `if`s e veja o que acontece.
Tente refazer esse programa sem usar `elif`.

## Estruturas de Repetição

São ferramentas de linguagens de programação utilizadas quando se quer repetir um trecho do código várias vezes.

```python
i = 0
while True:
    print(i)
    i = i + 1
```

### `while`

A estrutura do `while` na sua forma mais simples tem o seguinte formato.

```python
while condição:
    # Bloco de comandos
```

O commando funciona primeiramente fazendo uma avaliação da expressão na condição e caso seja considerada falsa o bloco de comandos é executado.
Ao final da execução do bloco de comandos, a condição é avaliada e o processo se repete.

A execução do bloco de comandos de uma estrutura de repetição também é chamada de _laço_.

> A condição só é avaliada antes da execução do bloco e entre o final da execução de um laço e antes da execução do próximo.

```python
# Imprime todos os números inteiros de 0 até 99
i = 0
while i < 100:
    print(i)
    i += 1
```

> É possível que uma estrutura de repetição faça com que o programa não acabe nunca, caso a condição para execução do laço não seja falsa.
>
> ```python
> i = 0
> while i < 1:
>     print(i) # Sem incrementar o i dentro do bloco, não tem como o i passar a valer mais do que 0
> ```

### `continue`

Ao encontrar a palavra `continue` o laço é interrompido como se tivesse terminado

```python
i = 0
while i < 10:
    print(i)
    i += 1
    continue # A instrução depois do continue nunca será executada
    print(i)
```

### `break`

Ao encontrar a palavra `break` o laço é interrompido e o próximo comando a ser executado é um imediatamente após o `while`.

```python
i = 0
while i < 1000:
    print(i)
    if i % 2 = 0:
        break
    i += 1
print("Fim")
```

O programa acima só irá imprimir o primeiro valor de `i` que é zero, após isso como, `i % 2 = 0` é verdadeira e o `break` é encontrado o laço é interrompido e a instrução `print("Fim")` é executada.

### Criando listas de coisas `list`

Uma lista em python é uma coleção de outros objetos.

```python
[1, "2", 10.3, 5, -2]
```

Listas podem ser atribuídas à variáveis da mesma forma que os outros objetos.

```python
lista = [1, "2", 10.3, 5, -2]
```

Para criar uma lista vazia podemos fazer `[]` ou `list()`.

> Não use `list` como nome de variável ou você não vai mais poder criar uma lista usando `list()`.

Listas podem conter outras listas como elementos.

```python
lista = [[1, 2], [3, 4], 5]
```

Para avaliar o valor guardado dentro de uma posição específica da lista podemos fazer `lista[i]` aonde `i` é o índice da posição.

> Em quase toda linguagem de programação toda lista/vetor/sequência começa com índice `0`.

```python
lista = ["a", "b", [1, 2], 3, 4]
print(lista[0])     # O resultado é a
print(lista[1])     # O resultado é b
print(lista)        # O resultado é ['a', 'b', 2, 3, 4]
print(lista[2])     # O resultado é [1, 2]
print(lista[2][0])  # O resultado é 1
```

Podemos adicionar elementos à uma lista com `nome_da_variável.append(elemento)` e remover com `nome_da_variável.pop(índice)`

```python
usuários = []
usuários.append("João")
usuários.append("George")
print(usuários)
usuários.pop(0)  # Remove o João
print(usuários)
```

### `for`

O `for` pode ser usado para executar um laço sobre todos os valores de uma lista ou outro objeto iterável.

```python
usuários = ["João", "George"]
for usuário in usuários:
    print("O usuário", usuário, "está cadastrado.")
```

O esqueleto do `for` funciona da seguinte forma:

```python
for variável in objeto_iterável:
    # Bloco de comandos
```

O `for` executa o bloco de comandos para cada valor do objeto iterável colocando esse valor na variável em cada execução do laço.

Uma forma praticamente equivalente de se escrever usando o `while` seria a logo abaixo.

```python
usuários = ["João", "George"]
i = 0
while i < len(usuários): # Aqui len calcula o tamanho da lista
    usuários = usuários[i]
    print("O usuário", usuário, "está cadastrado.")
    i += 1
```

A escolha entre o `for` e o `while` é mais subjetiva.
Via de regra, o `for` é utilizado quando se sabe antes do laço começar a executar, quantas vezes ele irá rodar.

> Os comandos `break` e `continue` também funcionam dentro de um `for`.

### `range`

A função `range` serve para construir objetos iteráveis (quase listas) que podem ser usadas para iterar sobre os números ou intervalos de números.

```python
print(range(10)) # vai mostrar só o objeto range
lista = list(range(10)) # cria uma lista com todos os resultados de range(10)
print(lista)
```

O código acima imprime na tela `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

Podemos então combinar um for com um range para mostrar todos os números pares até `10000`.

```python
for valor in range(10001):
    if valor % 2 == 0:
        print(valor)
```

Para ver mais sobre o range leia [a documentação](https://docs.python.org/pt-br/3/library/stdtypes.html#typesseq-range).

## Leitura Recomendada

Leia o restante do capítulo [Flow Control](https://automatetheboringstuff.com/2e/chapter2/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter2/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter2/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
