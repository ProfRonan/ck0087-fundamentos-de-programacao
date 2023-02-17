# Dicionários

Dicionário é um tipo de dado mutável que pode armazenar vários valores aonde os índices podem ser qualquer tipo _imutável_.
No caso de dicionários, os índices são chamados de **chaves**

> Imagine uma _lista_ a qual os índices não precisam ser números inteiros e sim, outras coisas, como _strings_.

```python
>>> usuário = {'nome': "João", "ano_nascimento": 2000}
>>> usuário['nome']
João
>>> usuário["ano_nascimento"]
2000
```

> A ordem das chaves de um dicionário não importa.
>
> ```python
> >>> listaA = [1, 2, 3]
> >>> listaB = [3, 1 ,2]
> >>> listaA == listaB
> False
> >>> dictA = {"nome": "Armando", "sangue": "O"}
> >>> dictB = {"sangue": "O", "nome": "Armando"}
> >>> dictA == dictB
> True
> ```

## Indexando e Fatiando

_Fatiamento_ **não existe** para um dicionário.

É possível tentar acessar uma chave inexistente no dicionário.
O erro será do tipo `KeyError`.

```python
>>> dictA = {"nome": "Zé", "endereço": "Rua Aqui"}
>>> dictA['número']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'número
```

### O Método `get`

Caso não saiba se a chave existe é possível acessar ele via o método `get`.

```python
>>> dictA = {"nome": "Zé", "endereço": "Rua Aqui"}
>>> dictA.get("número", 'S/N')
```

O resultado de `get(cahve, valor)` é o valor guardado no dicionário se a chave existir, ou o valor passado como argumento se ele não existir.

## Iterando Sobre Dicionários

Existem algumas formas de iterar sobre dicionários.

```python
usuário = {"nome": "Zé", "endereço": "Rua Aqui", "número": 1}
print("Pelas chaves")
for key in usuário.keys():
    print("\t", key)
print("Pelos valores")
for value in usuário.values():
    print("\t", value)
print("Os dois")
for key, value in usuário.items():
    print("\t", key, "com valor:", value)
```

Rode o [código acima](iterando.py) e veja o que é impresso na tela.

> Caso tente fazer o seguinte laço, o que vai ser considerado são as chaves do dicionário
>
> ```python
> usuário = {"nome": "Zé", "endereço": "Rua Aqui", "número": 1}
> print("Pelas chaves")
> for teste in usuário:
>     print(teste)
> ```

## Leitura Recomendada

Leia o restante do capítulo [Dictionaries and Structuring Data](https://automatetheboringstuff.com/2e/chapter5/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter5/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter5/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
