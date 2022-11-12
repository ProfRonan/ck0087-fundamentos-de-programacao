"""funcionalidades necessárias para adicionar disciplina ao banco"""

import json

LOCAL_ARQUIVO = "./data/disciplinas.json"


def criar(código: str, nome: str):
    if not type(código) == str:
        raise TypeError("código tem que ser string")
    if not type(nome) == str:
        raise TypeError("nome tem que ser string")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    for disciplina in disciplinas:
        if disciplina["código"] == código:
            raise BaseException("disciplina com código dado ja existe")

    disciplina = {
        "código": código,
        "nome": nome
    }
    with open(LOCAL_ARQUIVO, "a", encoding="utf8") as file:
        json.dump(disciplina, file)

    return disciplina
