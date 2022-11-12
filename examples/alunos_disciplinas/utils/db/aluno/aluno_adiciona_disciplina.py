import json

from aluno_ler import ler as ler_aluno
from ..disciplina.disciplina_ler import ler as ler_disciplina

LOCAL_ARQUIVO = "./data/alunos.json"


def adiciona_disciplina(matrícula: int, código: str):
    if not type(matrícula) == int:
        raise TypeError("matrícula tem que ser inteiro")
    if not type(código) == str:
        raise TypeError("código tem que ser string")

    if not ler_aluno(matrícula):
        raise BaseException("aluno inexistente no banco de dados")

    if not ler_disciplina(código):
        raise BaseException("disciplina inexistente no banco de dados")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    for aluno in alunos:
        if aluno["matrícula"] == matrícula:
            aluno["disciplinas"].append(código)
            break

    with open(LOCAL_ARQUIVO, "w", encoding="utf8") as file:
        json.dump(alunos, file)

    return aluno
