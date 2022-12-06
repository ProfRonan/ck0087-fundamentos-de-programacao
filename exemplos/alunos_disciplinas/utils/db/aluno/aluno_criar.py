"""funcionalidades necessárias para adicionar aluno ao banco"""

import json

LOCAL_ARQUIVO = "./data/alunos.json"


def gerar_matrícula():
    """Gera um número de matrícula que não existe no banco"""
    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    maior = 0
    for aluno in alunos:
        if maior < aluno["matrícula"]:
            maior = aluno["matrícula"]

    return maior + 1


def criar(nome: str):
    """Adiciona aluno com nome dado no banco de dados"""

    if not type(nome) == str:
        raise TypeError("nome tem que ser string")
    aluno = {
        "nome": nome,
        "matrícula": gerar_matrícula()
    }

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    alunos.append(aluno)

    with open(LOCAL_ARQUIVO, "w", encoding="utf8") as file:
        json.dump(alunos, file, ensure_ascii=False)

    return aluno
