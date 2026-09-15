from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

clientes = [
    {"id": 1, "nome": "Ana Silva", "email": "ana@email.com", "empresa": "Ana Design"},
    {"id": 2, "nome": "Carlos Souza", "email": "carlos@email.com", "empresa": "CS Tech"},
    {"id": 3, "nome": "Marina Costa", "email": "marina@email.com", "empresa": "Marina Store"},
]

pedidos = [
    {"id": 1001, "cliente": "Ana Silva", "produto": "Site institucional", "valor": 2500, "status": "Concluído"},
    {"id": 1002, "cliente": "Carlos Souza", "produto": "Sistema web", "valor": 4800, "status": "Em andamento"},
    {"id": 1003, "cliente": "Marina Costa", "produto": "Landing page", "valor": 1200, "status": "Pendente"},
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/dashboard")
def dashboard():
    faturamento = sum(p["valor"] for p in pedidos)

    return jsonify({
        "clientes": len(clientes),
        "pedidos": len(pedidos),
        "faturamento": faturamento,
        "pedidos_concluidos": len(
            [p for p in pedidos if p["status"] == "Concluído"]
        )
    })


@app.route("/api/clientes")
def listar_clientes():
    busca = request.args.get("busca", "").lower()

    resultado = [
        cliente for cliente in clientes
        if busca in cliente["nome"].lower()
        or busca in cliente["empresa"].lower()
    ]

    return jsonify(resultado)


@app.route("/api/pedidos")
def listar_pedidos():
    return jsonify(pedidos)


@app.route("/api/clientes", methods=["POST"])
def criar_cliente():
    dados = request.json

    if not dados or not dados.get("nome") or not dados.get("email"):
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": dados["nome"],
        "email": dados["email"],
        "empresa": dados.get("empresa", "Não informado")
    }

    clientes.append(novo_cliente)

    return jsonify(novo_cliente), 201


if __name__ == "__main__":
    app.run(debug=True)
