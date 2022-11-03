import json
"""Para rodar esse servidor flask rode o commando `flask --debug --app ./examples/flask-server.py run`"""

from flask import Flask, Response, request

app = Flask(__name__)

# Variável global que guardará os usuário do sistema.
usuários: list[dict] = []


# Cada rota do servidor web pode ser criada utilizando esses "decoradores" de rota.
@app.route("/", methods=["GET"])
def show_endpoints():
    """Função que mostra todos os pontos de saída da api."""
    endpoints = {
        "/": {"GET": "Retorna essa lista de pontos."},
        "/user": {"GET": "Retorna a lista de usuários do sistema.", "POST": "Cria um novo usuário no sistema. No corpo da requisição tem que ser enviado um nome de usuário e uma senha."},
        "/user/login": {"POST": "Faz o login do usuário no sistema. Quando no corpo da mensagem tem o nome do usuário e a senha. No estilo {\"nome\": \"NOME_DO_USUÁRIO\", \"senha\": \"senha\"}"}
    }
    response = Response(json.dumps(endpoints), status=200,
                        content_type="application/json")
    return response


@app.route("/user", methods=["GET"])
def get_user():
    """Função que lida SOMENTE com listar os usuário do sistema."""
    lista_usuários = {"usuários": [user.get("nome", "") for user in usuários]}
    return Response(json.dumps(lista_usuários), status=200, content_type="application/json")


@app.route("/user", methods=["POST"])
def create_user():
    """Função que lida SOMENTE com criar um usuário no sistema."""
    global usuários
    novo_usuário = request.json
    if not isinstance(novo_usuário, dict):
        return Response("O corpo da mensagem tem que ser um objeto/dicionário.")
    if not novo_usuário:
        return Response("Usuário tem que ser um json válido com nome e senha.", status=400)
    nome = novo_usuário.get("nome", "")
    if not nome:
        return Response("Nome do usuário não pode ser vazio.", status=400)
    senha = novo_usuário.get("senha", "")
    if not senha:
        return Response("Senha do usuário não pode ser vazia.", status=400)

    # Se um usuário já existir com esse nome, não será possível criar outro com o mesmo nome.
    for usuário in usuários:
        if usuário["nome"] == nome:
            return Response(f"Usuário com nome {nome} já cadastrado no sistema.", status=422)

    # Adiciona o usuário à lista de usuários do sistema.
    usuários.append(novo_usuário)

    return Response(json.dumps(novo_usuário), status=201, content_type="application/json")
