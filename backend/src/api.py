from flask import Flask, request, jsonify
from flask_cors import CORS
from matriz import Matriz

app = Flask(__name__)
CORS(app)

@app.route("/resolver", methods=["POST"])
def resolver_matriz():
    data = request.get_json()
    valores = data.get("valores")
    ordem = data.get("ordem")

    matriz = Matriz(valores, ordem)
    matriz.montar_matriz()
    det = matriz.calcular_determinante()
    
    resposta = {
        "matriz": matriz.matriz,
        "determinante": det
    }

    if det != 0:
        A = matriz.calcular_crammer()
        resposta["cramer"] = A

    return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)
