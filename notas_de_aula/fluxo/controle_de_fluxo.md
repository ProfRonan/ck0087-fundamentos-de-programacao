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

TODO: Escrever Texto

### `while`

TODO: Escrever Texto

### `continue`

TODO: Escrever Texto

### `break`

TODO: Escrever Texto

### `for`

TODO: Escrever Texto

### `range`

TODO: Escrever Texto

### `list`

TODO: Escrever Texto

## Leitura Recomendada

Leia o restante do capítulo [Flow Control](https://automatetheboringstuff.com/2e/chapter2/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter2/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter2/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
