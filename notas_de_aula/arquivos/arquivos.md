# Arquivos

A memória RAM só vai armazenar os arquivos enquanto o programa estiver rodando no computador.

Para ter persistência, teremos que usar algum dispositivo de armazenamento persistente, como o SSD (solid state drive) ou o HD (hard drive).

## `open`

Uma função embutida de Python que pode ser usada para abrir/criar arquivos.

Leia atentamente o [tutorial](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#tut-files) e posteriormente a [documentação](https://docs.python.org/pt-br/3/library/functions.html#open) da função.

Antes de trabalhar com o `open` lembre-se:

> Grandes poderes, também trazem grandes responsabilidades.
>
> — <cite>Amazing Fantasy 15 (Stan Lee)</cite>

Se você fizer `open("arquivo_muito_importante", "w")` diga **_ADEUS_** ao conteúdo do seu arquivo, sem chance de recuperar, sem perdão, sem volta.

Também é **_IMPORTANTE_** saber que ao passar `open("./arquivo")` o diretório relativo usado é aquele em que o interpretador foi _invocado_.
Ou seja, pode não ser o que você está imaginando.

## A biblioteca `pathlib`

O caminho completo do diretório atual do _console_ pode ser encontrado usando o comando `pwd` que funciona tanto no `Linux (Bash)` quanto no `Windows (PowerShell)`.

Por exemplo, o caminho completo esse arquivo, no meu computador local que está com o Ubuntu/Linux instalado se encontra no diretório: `/home/seuronao/projects/profronan/ck0087-fundamentos-de-programacao/notas_de_aula/arquivos`.

Como os sistemas operacionais diferem na forma que exibem trabalham com diretórios, Python tem uma biblioteca embutida que permite trabalhar com diretórios abstraindo qual sistema operacional subjacente está rodando o interpretador.

A documentação oficial da biblioteca `pathlib` pode ser encontrada [aqui](https://docs.python.org/pt-br/3/library/pathlib.html).

## Leitura Recomendada

Leia o restante do capítulo [Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) existe a tradução automática do google para páginas inteiras como pode ser visto [clicando aqui](https://automatetheboringstuff-com.translate.goog/2e/chapter9/?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp).

## Créditos

Esse texto foi fortemente inspirado no [Automate The Boring Stuff](https://automatetheboringstuff.com/2e/chapter9/) e também está sob a licença [Creative Commons](https://creativecommons.org/licenses/by-nc-sa/3.0/).
