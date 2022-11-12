"""Ler aluno do banco"""

import json

LOCAL_ARQUIVO = "./data/alunos.json"


def ler(matrícula: int):
    """Lê aluno do banco com matrícula dada ou nome dado."""

    if not type(matrícula) == int:
        raise TypeError("matrícula tem que ser inteiro")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)
    for aluno in alunos:
        if aluno["matrícula"] == matrícula:
            return aluno
    return None


def listar(nome: str):
    """Lista todos os alunos que tem nome."""

    if not type(nome) == str:
        raise TypeError("nome tem que ser string")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    # Retorna os elementos da lista que tem a chave nome igual ao
    # nome dado como argumento
    return list(filter(lambda x: x["nome"] == nome, alunos))
