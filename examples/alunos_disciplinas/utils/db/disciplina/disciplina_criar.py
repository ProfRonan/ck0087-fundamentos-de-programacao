"""funcionalidades necessárias para adicionar disciplina ao banco"""

import json

LOCAL_ARQUIVO = "./data/disciplinas.json"


def criar(codigo: str, nome: str):
    if not codigo.isinstance(str):
        raise TypeError("codigo tem que ser string")
    if not nome.isinstance(str):
        raise TypeError("nome tem que ser string")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            raise BaseException("disciplina com codigo dado ja existe")

    disciplina = {
        "codigo": codigo,
        "nome": nome
    }
    with open(LOCAL_ARQUIVO, "a", encoding="utf8") as file:
        json.dump(disciplina, file)

    return disciplina
