"""Ler disciplina do banco"""

import json

LOCAL_ARQUIVO = "./data/disciplinas.json"


def ler(codigo: str):
    if not codigo.isinstance(str):
        raise TypeError("codigo tem que ser string")
    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            return disciplina
    return None


def listar(nome: str):
    if not nome.isinstance(str):
        raise TypeError("nome tem que ser string")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    return list(filter(lambda x: x["nome"] == nome, disciplinas))
