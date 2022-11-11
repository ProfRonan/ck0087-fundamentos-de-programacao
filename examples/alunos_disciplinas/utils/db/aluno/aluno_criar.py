"""funcionalidades necessárias para adicionar aluno ao banco"""

import json

LOCAL_ARQUIVO = "./data/alunos.json"


def gerar_matricula():
    """Gera um número de matricula que não existe no banco"""
    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    maior = 0
    for aluno in alunos:
        if maior < aluno["matricula"]:
            maior = aluno["matricula"]

    return maior + 1


def criar(nome: str):
    """Adiciona aluno com nome dado no banco de dados"""

    if not nome.isinstance(str):
        raise TypeError("nome tem que ser string")
    aluno = {
        "nome": nome,
        "disciplinas": [],
        "matricula": gerar_matricula()
    }
    with open(LOCAL_ARQUIVO, "a", encoding="utf8") as file:
        json.dump(aluno, file)

    return aluno
