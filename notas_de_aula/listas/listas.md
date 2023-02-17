# Listas

Listas são sequências de valores.

```python
[1, 2, 3]
["a", "b", "c"]
[1, "a", 2, "b"] # Podem incluir tipos diferentes
[[0, 1], [2, 3]] # Podem incluir outras listas
```

## Atribuição

Listas podem ser atribuídas à variáveis usando o operador de atribuição normalmente.

```python
lista1 = [1, 2, 3, 4, 5] # Pode-se guardar uma referência para uma lista com o operador de atribuição

listaVazia = [] # Pode-se declarar uma lista vazia assim
listaVazia = list() # Ou assim

# Listas podem ter valores arbitrários.
lista2 = ["Banana", 1, True, ["Outra", "Lista", "Dentro"]]
```

## Adicionar e Remover

Listas são objetos mutáveis, então é possível alterar o valor deles depois que eles foram criados.

```python
# Adicionando valores à uma lista já criada
exemplo = [0] # exemplo => [0]
exemplo.append(2)  # exemplo => [0, 2]
exemplo.append(1) # exemplo => [0, 2, 1]
exemplo.append("Abacate") # exemplo => [0, 2, 1, "abacate"]

# Removendo valores de uma lista já criada
exemplo.pop()  # remove o último item da lista
# exemplo => [0, 2 ,1]
exemplo.pop(1)  # remove o "segundo" item da lista
# exemplo => [0, 1]
```

## Indexando e Fatiando Listas

Uma posição especifica de uma lista pode ser obtida assim `lista[posição]`.
Chamamos essa posição do índice de um elemento da lista.

```python
>>> indexando = [x for x in range(1, 12)] # indexando => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> indexando[0]
1
>>> indexando[2]
3
>>> indexando[4]
5
```

> Os vetores/string/listas em quase toda linguagem de programação começam do índice zero.

### Índices com Números Negativos

O que acontece quando os índices são negativos?

```python
>>> vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
>>> vogais[-1]
'u'
>>> vogais[-2]
'o'
>>> vogais[-3]
'i'
>>> vogais[-9]
'E'
```

### Fatiando Listas

Podemos **"pegar"** pedaços de uma lista usando o operador _slice_ (fatia).

O operador funciona da seguinte forma `lista[inicio:fim:passo]`, todos os elementos são opcionais com valores padrões `0`, `len(lista)` e `1` respectivamente.
Uma operação _slice_ faz uma cópia _rasa_ da lista.

```python
>>> números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> números[0:5]
[0, 1, 2, 3, 4]
>>> números[0:1]
[0]
>>> números[0:10:2]
[0, 2, 4, 6, 8]
>>> números[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> números[::2]
[0, 2, 4, 6, 8]
>>> números[1::2]
[1, 3, 5, 7, 9]
>>> números[:3:4]
[0]
>>> números[-1:-5] # Aqui o resultado é vazio, pois o passo é positivo se não especificado
[]
>>> números[-1:-5:-1]
[9, 8, 7, 6]
>>> números[-1::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## O que significa ser mutável

Um valor mutável é aquele tipo de variável que pode ser alterada depois de atribuída.
Alguns exemplos em Python: `list`, `dict`, `set`, ...

```python
>>> listA = [1, 2, 3]
>>> listB = listA
>>> listA
[1, 2, 3]
>>> listB
[1, 2, 3]
>>> listA.append(4)
>>> listB
[1, 2, 3, 4]
```

### Consequências

Quando você passa uma lista para uma função, ao final da função talvez sua lista passada como argumento seja alterada!

```python
def lista_quadrada(lista):
    """
    Pega cada elemento da lista passada como argumento e faz ele virar o quadrado dele mesmo.
    """
    for i in range(len(lista)):
        lista[i] *= i


lista_teste = [1, 2, 3, 4, 5]
lista_quadrada(lista_teste)
print(lista_teste)
```

O resultado desse programa é `[0, 2, 6, 12, 20]`.
O código pode ser encontrado [aqui](mutabilidade.py).

## Operações

### Concatenação `+`

Cria uma lista nova adicionando os elementos da segunda lista ao final da primeira.

```python
>>> lista = [1, 2, 3] + [1, 2, 4, 8] + [0, -2, 4]
>>> lista
[1, 2, 3, 1, 2, 4, 8, 0, -2, 4]
```

### Repetição `*`

Cria uma lista nova que é formada pela cópia de uma lista um número inteiro de vezes.

```python
>>> lista = [1, 2, 3] * 5
>>> lista
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
```

> Cuidado modificar uma _"cópia"_ de uma lista, na realidade, é modificar o resultado da referência dela.
>
> ```python
> >>> lista = [[1], [2]] * 4
> >>> lista
> [[1], [2], [1], [2], [1], [2], [1], [2]]
> >>> lista[0].append(3) # Adiciona 3 ao final da primeira lista dentro da lista
> >>> lista
> [[1, 3], [2], [1, 3], [2], [1, 3], [2], [1, 3], [2]]
> ```

## Iterando sobre **listas**

Existem algumas maneiras convenientes de iterar sobre os elementos de uma lista.

Um `for` simples.

```python
lista = [1, 2, 3, 4, 5, 6]
for x in lista:
    print(x)
```

Um `for` usando um índice que vá do inicio até o final da lista.
Pouco legível, mas, às vezes, é o único jeito.

```python
lista = [1, 2, 3, 4, 5, 6]
for i in range(len(lista)):
    print(lista[i])
```

Um `for` usando o `enumerate`.

```python
lista = [1, 2, 3, 4, 5, 6]
for i, x in enumerate(lista):
    print("lista na posição:", i, "tem elemento", x)
```

## Métodos

Para ver todos os métodos que envolvem as listas em Python veja a [documentação oficial](https://docs.python.org/pt-br/3/tutorial/datastructures.html#more-on-lists).

## Compreensão de listas

Para saber mais como utilizar a compreensão de listas:

```python
>>> lista = [x for x in range(10)]
>>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista = [x**2 for x in range(10)]
>>> lista
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> lista = [x for x in range(10) if x % 2 == 0]
>>> lista
[0, 2, 4, 6, 8]
```

Também é recomendado ver a [documentação oficial](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list-comprehensions).

## Leitura Recomendada

Leia o restante do capítulo [Lists](https://automatetheboringstuff.com/2e/chapter4/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter4/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter4/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
