# Strings (cadeia de caracteres)

Uma introdução geral à manipulação de strings.

```python
print("Olá!")
print("--------")
print("Podemos ter um enter\ndentro da string.")
print("--------")
print("Podemos ter um tab\ttambém dentro da string.")
print("--------")
print("Aspas simples \' e aspas duplas podem ser escritas também \".")
print("--------")
print("A própria barra invertida também pode ser escapada \\.")
```

Rode esse [código acima](prints.py) como um script e veja como se comportam cada um desses `print`s.

## Atribuição

Strings são imutáveis.

> Uma string construída jamais pode ser alterada.
> Contudo, o conteúdo de uma variável pode ser descartado e uma nova string pode ser colocada no lugar.
> Então é possível pegar uma string e criar uma nova baseada na anterior.
>
> ```python
> >>> frase = "Quem não tem nada a temer"
> >>> frase = frase + ", tem muito o que esconder, especialmente das pessoas que tem algo a temer."
> >> frase
> 'Quem não tem nada a temer, tem muito o que esconder, especialmente das pessoas que tem algo a temer.'
> ```

## Operações

A concatenação `+` e a repetição `*` funcionam da mesma maneira que nas _listas_ veja [Listas](../listas/listas.md) para relembrar.

## Indexando e Fatiando

A _indexação_ e a operação de _fatiar_ uma string funciona da mesma maneira que nas _listas_ veja [Listas](../listas/listas.md) para relembrar.

> Um único detalhe é que não é possível alterar uma `string` já formada.
>
> ```python
> >>> lista = [1, 2]
> >>> lista[0] = 3
> >>> lista
> [3, 2]
> >>> frase = "ab"
> >>> frase[0] = "c"
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: 'str' object does not support item assignment
> ```

## Múltiplas linhas

Se por acaso, você precisa definir uma _string_ em várias linhas, pois ela é muito grande, é possivel usar `"""STRING"""` para isso

```python
aspas_triplas = """Aspas triplas (simples ou duplas)
                   Servem para podermos escrever strings em
                   muitas linhas!"""
print(aspas_triplas)

outro_jeito = "Um outro jeito\n\
              de se escrever strings\n\
              que passem de muitas linhas\n\
              sem usar aspas triplas\n\
              é colocando o \\ no final de cada linha."
print(outro_jeito)
```

> Os espaços em branco são preservados entre as múltiplas linhas.
> Se isso for um problema, veja as bibliotecas [textwrap](https://docs.python.org/3/library/textwrap.html) e [inspect](https://docs.python.org/3/library/inspect.html) se quiser lidar com isso.

## O que significa ser imutável de verdade?

Um valor imutável é aquele tipo de variável que não pode ser alterada.
Alguns exemplos em Python: `int`, `float`, `str`, `frozenset`...

```python
a = "Primeira"
b = "Primeira"
c = a
print(id(a))  # id(variável) resulta na posição da memória dessa variável.
print(id(b))
print(id(b) == id(a)) # Como as duas são iguais e não podem ser alteradas, dá pra economizar memória colocando tudo no mesmo lugar
print(id(c))
print(id(c) == id(a)) # c é a mesma string também... coloca no mesmo lugar para economizar memória
```

O código do programa acima pode ser visto [aqui](imutabilidade.py).

## Estar ou não estar, eis a questão!

Breves exemplos de uso dos operadores `in` e `not in`.
Ele verifica se `sub_string in string` se a `sub_string` aparece dentro, em alguma parte, da string.

> Esses operadores também podem ser usados com listas, mas no caso de listas, `valor in lista`, eles verificam se o `valor` aparece ou não como elemento da `lista`.

```python
>>> frase_motivacional = "#Vai dar certo!"
>>> "Vai" in frase_motivacional
True
>>> "vai" in frase_motivacional
False
>>> " " in frase_motivacional
True
>>> " dar" in frase_motivacional
True
>>> "#certo" in frase_motivacional
False
>>> "#" in frase_motivacional
True
>>> "tristeza" not in frase_motivacional
True
```

## Prefixos lidando com Strings

Antes de começar uma string por exemplo `"Hoje, vai ser um bom dia."`.
Tem formas de _"alterar"_ a como o interpretador lida com ela colocando um prefixo antes das primeiras aspas, alguns exemplos são `r`, `b`, `f` e `u`.

```python
# Com o prefixo r ou R o interpretador pega a string "crua" sem fazer qualquer análise ou mudança nos caracteres dela como por exemplo trocar o "\n" por um enter.
prefixoR = r'Pode escrever tudo \asdf \n com qualquer coisa que {#$34)(U*#!@#&*} não vai ser alterado \o12 \hAF'
print(prefixoR)

# O prefixo f ou F serve para formatar a string substituindo valores de dentro dela por resultados de expressões.
dia = "Hoje"
tempo = "bom"
graus = 29
atividades = ["ir ao supermercado", "ganhar no LoL"]
prefixoF = f'{dia} vai ser {tempo} fazendo {graus}° e você tem que:\n {atividades}'
print(prefixoF)

# O prefixo b guarda a representação em binário de uma string.
prefixoB = b'\xE2\x82\xAC'
prefixoB = prefixoB.decode("utf-8") # Converte essa representação de volta em utf-8
print(prefixoB)
```

> No caso o Python3 já usa utf-8 como padrão não sendo necessário usar string binária, exceto em casos muito específicos.
>
> O prefixo `u` também é usado para manipular Unicode.

## Formatando Strings

Existem formas criar strings _com valores obtidos_ sem ser concatenando um monte delas.

```python
>>> dia = "Hoje"
>>> tempo = "bom"
>>> graus = 29
>>> atividades = ["ir ao supermercado", "ganhar no LoL"]
>>> resultado = dia +  " vai ser " + tempo + " fazendo " + str(graus) + "° e você tem que:\n " + str(atividades)
>>> resultado
"Hoje vai ser bom fazendo 29° e você tem que:\n ['ir ao supermercado', 'ganhar no LoL']"
```

> Muito chato e feio escrever assim, mas é possível.

Para fazer de forma mais elegante e eficiente podemos usar outras técnicas.

```python
# Sem os números a ordem natural é da esquerda pra direita.
>>> TEMPLATE = "Hoje é {0} de {1}, {2}"
>>> TEMPLATE
'Hoje é {0} de {1}, {2}'
>>> dia = 27
>>> mes = "Fevereiro"
>>> ano = "2022"
>>> preenchido = TEMPLATE.format(dia, mes, ano)
>>> preenchido
'Hoje é 27 de Fevereiro, 2022'
>>> AMANHA = "Amanhã, no mês de {1} será dia {0}"
>>> AMANHA.format(dia, mes)  # O primeiro parâmetro refere ao número zero.
'Amanhã, no mês de Fevereiro será dia 27'
```

Existem várias formas de apresentar os valores quando formatamos uma string, seja com o método `format` ou usando `f-strings`.

Uma lista exaustiva pode ser encontrada na [documentação oficial](https://docs.python.org/3/library/string.html#custom-string-formatting).

A forma mais comum de ter que mudar a apresentação do resultado de uma expressão é quando queremos apresentar resultados envolvendo números flutuantes ou aproximações de números irracionais.

```python
>>> import math
>>> pi = math.pi
>>> tentativa = f"O valor de pi é {pi}"
'O valor de pi é 3.141592653589793'
>>> mudando_precisão = f"O valor de pi é {pi:10.2f}"
>>> mudando_precisão
'O valor de pi é       3.14'
>>> f"{pi:10}"
'3.141592653589793'
>>> f"{pi:2.2f}"
'3.14'
```

## Métodos

Existem vários métodos prontos para facilitar o trabalho e manuseio de `strings` veja a [documentação oficial](https://docs.python.org/3/library/stdtypes.html#string-methods) para encontrar todos eles.

## Leitura Recomendada

Leia o restante do capítulo [Manipulating Strings](https://automatetheboringstuff.com/2e/chapter6/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter5/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter5/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
