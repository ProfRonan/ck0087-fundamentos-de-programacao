"""Ler disciplina do banco"""

import json

LOCAL_ARQUIVO = "./data/disciplinas.json"


def ler(código: str):
    if not type(código) == str:
        raise TypeError("código tem que ser string")
    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    for disciplina in disciplinas:
        if disciplina["código"] == código:
            return disciplina
    return None


def listar(nome: str):
    if not type(nome) == str:
        raise TypeError("nome tem que ser string")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        disciplinas = json.load(file)

    return list(filter(lambda x: x["nome"] == nome, disciplinas))
