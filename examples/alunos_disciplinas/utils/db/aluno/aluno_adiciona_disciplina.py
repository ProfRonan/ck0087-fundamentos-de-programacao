import json

from aluno_ler import ler as ler_aluno
from ..disciplina.disciplina_ler import ler as ler_disciplina

LOCAL_ARQUIVO = "./data/alunos.json"


def adiciona_disciplina(matricula: int, codigo: str):
    if not type(matricula) == int:
        raise TypeError("matricula tem que ser inteiro")
    if not type(codigo) == str:
        raise TypeError("codigo tem que ser string")

    if not ler_aluno(matricula):
        raise BaseException("aluno inexistente no banco de dados")

    if not ler_disciplina(codigo):
        raise BaseException("disciplina inexistente no banco de dados")

    with open(LOCAL_ARQUIVO, encoding="utf8") as file:
        alunos = json.load(file)

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            aluno["disciplinas"].append(codigo)
            break

    with open(LOCAL_ARQUIVO, "w", encoding="utf8") as file:
        json.dump(alunos, file)

    return aluno
