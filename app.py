#import numpy
from flask import Flask, request, jsonify
from calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)

'''
@app.route("/demo-ruff")
def demo_ruff():
    resultado_temporal = "variable local no utilizada"
    return jsonify({"mensaje": resultado_temporal})
'''

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "calculadora-ci"
    }), 200


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Calculadora CI funcionando",
        "operaciones": {
            "sumar": "/sumar?a=2&b=3",
            "restar": "/restar?a=10&b=4",
            "multiplicar": "/multiplicar?a=3&b=5",
            "dividir": "/dividir?a=10&b=2",
            "health": "/health"
        }
    })


@app.route("/sumar")
def endpoint_sumar():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"resultado": sumar(a, b)})


@app.route("/restar")
def endpoint_restar():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"resultado": restar(a, b)})


@app.route("/multiplicar")
def endpoint_multiplicar():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify({"resultado": multiplicar(a, b)})


@app.route("/dividir")
def endpoint_dividir():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 1))

    try:
        resultado = dividir(a, b)
        return jsonify({"resultado": resultado})
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(debug=True)