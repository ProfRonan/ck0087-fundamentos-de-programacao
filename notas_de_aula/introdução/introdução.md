# Introdução

## Pra que programar?

- Reorganizar centenas de milhares de arquivos no computador.
- Preencher e enviar centenas de emails ou formulários de forma automática.
- Avisar toda vez que um produto em um site muda de preço.
- Fazer o computador enviar notificações quando algo acontece.
- Atualizar e modificar planilhas.
- Verificar o e-mail e responder de forma automática alguns deles.

## O que é programar

É escrever uma série de regras, passos ou instruções que o computador deve executar.

- "Faça isso e depois faça aquilo."
- "Se uma algo é verdade, então faça isso; senão faça outra coisa."
- "Faça uma ação exatamente 213 vezes."
- "Faça uma ação enquanto algo é verdade."

```python
# Exemplo 1
# Programa em python que verifica se uma senha é verdadeira e responde de acordo.

arquivo_senha = open('arquivo_com_senhas.txt')
senha = arquivo_senha.read()
print("Escreva sua senha:")
senha_digitada = input()
if senha == senha_digitada:
    print("Autorizado.")
else:
    print("Acesso negado.")
```

## Python

[Python](https://www.python.org/) é uma linguagem de programação.

Uma linguagem de programação é um conjunto de regras sintáticas definido por quem é o _"dono"_ da linguagem.

Exemplos de violação de regra sintática em português:

- "emchergar": não é uma palavra válida em português.
- "Nós vai": a concordância verbal foi violada.

É possível ter uma frase sintaticamente correta mas sem sentido semântico:

> O vento do duende vem de roxo quando pisca a inconsciência do javali.

## Interpretador

Um programa escrito em Python é um texto que segue as regras sintáticas da linguagem.

Um **interpretador** de python é um programa de computador que recebe um programa escrito em python e executa as instruções contidas nesse programa.

## Erros

**Erros sintáticos** são erros que violam as regras sintáticas definidas pela linguagem.

**Erros semânticos** são erros quando um programa não faz o que o programador dele _gostaria_ que ele fizesse.

Só tem um deles que o computador é capaz de identificar.
Dica: um computador não adivinha pensamentos.

**Bugs** são erros semânticos em sua grande maioria.

> É possível ter um erro semântico aonde o interpretador executa uma instrução erroneamente, mas isso é um problema dos programadores que escreveram o código do interpretador.

## Leitura Recomendada

Leia o restante do capítulo [Introdução](https://automatetheboringstuff.com/2e/chapter0/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter0/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter0/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
