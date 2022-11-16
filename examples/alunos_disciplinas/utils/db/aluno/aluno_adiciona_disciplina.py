import json

from .aluno_ler import ler as ler_aluno
from ..disciplina.disciplina_ler import ler as ler_disciplina

LOCAL_ARQUIVO = "./data/alunos.json"
LOCAL_TABELA_LIGACAO = "./data/aluno_disciplina.json"


def adiciona_disciplina(matrícula: int, código: str):
    if not type(matrícula) == int:
        raise TypeError("matrícula tem que ser inteiro")
    if not type(código) == str:
        raise TypeError("código tem que ser string")

    aluno = ler_aluno(matrícula)
    if not aluno:
        raise BaseException("aluno inexistente no banco de dados")

    disciplina = ler_disciplina(código)
    if not disciplina:
        raise BaseException("disciplina inexistente no banco de dados")

    with open(LOCAL_TABELA_LIGACAO, encoding="utf8") as file:
        aluno_disciplina = json.load(file)
    
    for valor in aluno_disciplina:
        if valor["matrícula"] == matrícula and valor["código"] == código:
            raise BaseException("aluno já está matriculado nessa disciplina")
    
    valor = {
        "matrícula": matrícula,
        "código": código
    }

    aluno_disciplina.append(valor)

    with open(LOCAL_TABELA_LIGACAO, "w", encoding="utf8") as file:
        json.dump(aluno_disciplina, file, ensure_ascii=False)

    return valor