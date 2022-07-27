from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#lista de usuários
usuariosDados = {
    1: {
        "id": 1,
        "nome": "Leandro"
    },
    2: {
        "id": 2,
        "nome": "Ana"
    }
}

def usuariosResposta():
    return {"usuarios": list(usuariosDados.values())}

@app.route("/")
def root():
    return "<h1>API com Flask</h1>"

@app.route("/usuarios")
def listarUsuarios():
    return usuariosResposta()

#buscar por um usuário
@app.route("/usuarios/<int:usuarioId>")
def buscar(usuarioId: int):
    usuario = usuariosDados.get(usuarioId)

    if usuario:
        return usuariosDados[usuarioId]
    else:
        return "Usuário não encontrado"

#cadastrar um novo usuário por nome
@app.route("/usuarios", methods=["POST"])
def cadastrarUsuario():
    body = request.json
    ids = list(usuariosDados.keys())
    nome = body.get("nome")

    if ids:
        novaId = ids[-1] + 1
    else:
        novaId = 1
    
    usuariosDados[novaId] = {
        "id": novaId,
        "nome": body["nome"]
    }
    return "Usuário: {0}, cadastrado com sucesso".format(nome)

#apagar nome de um usuário existente
@app.route("/usuarios/<int:usuarioId>", methods=["DELETE"])
def apagar(usuarioId: int):

    if usuarioId in usuariosDados:
        del usuariosDados[usuarioId]
        return "Usuário: {0}, foi excluído".format(usuarioId)
    else:
        return "Usuário não encontrado"

#atualizar um usuário existene
@app.route("/usuarios/<int:usuarioId>", methods=["PUT"])
def atualizar(usuarioId: int):
    body = request.json
    nome = body.get("nome")

    if usuarioId in usuariosDados:
        usuariosDados[usuarioId]["nome"] = nome
        return "Usuário: {0}, foi atualizado com o nome: {1}".format(usuarioId, nome)
    else:
        return "Usuário não encontrado"
    
        
app.run(debug=True)