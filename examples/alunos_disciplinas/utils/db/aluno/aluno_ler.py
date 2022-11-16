"""Ler aluno do banco"""

import json

LOCAL_ARQUIVO = "./data/alunos.json"
LOCAL_TABELA_LIGACAO = "./data/aluno_disciplina.json"


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

def procurar(nome: str):
    """Lista todos os alunos que tem nome contento o argumento dado."""

    if not type(nome) == str:
        raise TypeError("nome tem que ser string")
    
    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)
    
    return list(filter(lambda x: nome in x["nome"], alunos))

def disciplinas_matriculadas(matrícula: int):
    """Retorna a lista de disciplinas que o aluno com a matrícula dada está matriculado."""

    if not type(matrícula) == int:
        raise TypeError("matrícula tem que ser um inteiro")

    aluno = ler(matrícula)
    if not aluno:
        raise BaseException("aluno inexistente")
    
    with open(LOCAL_TABELA_LIGACAO, encoding="utf8") as file:
        aluno_disciplina = json.load(file)
    
    matriculadas = []

    for disciplina in filter(lambda x: x["matrícula"] == matrícula, aluno_disciplina):
        matriculadas.append(disciplina["código"])

    return matriculadas