from flask import Flask, jsonify, render_template, request
from modelo import predecir_estado
from datetime import datetime
import json
import os

app = Flask(__name__)

STATS_FILE = "stats.json"


def cargar_estadisticas():
    if not os.path.exists(STATS_FILE):
        return {
            "predicciones": [],
            "conteo_categorias": {},
            "ultima_prediccion": None
        }

    with open(STATS_FILE, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_estadisticas(estadisticas):
    with open(STATS_FILE, "w", encoding="utf-8") as archivo:
        json.dump(estadisticas, archivo, indent=4, ensure_ascii=False)


def registrar_prediccion(resultado, entradas):
    estadisticas = cargar_estadisticas()

    nueva_prediccion = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado_predicho": resultado,
        "entradas": entradas
    }

    estadisticas["predicciones"].append(nueva_prediccion)

    if resultado not in estadisticas["conteo_categorias"]:
        estadisticas["conteo_categorias"][resultado] = 0

    estadisticas["conteo_categorias"][resultado] += 1
    estadisticas["ultima_prediccion"] = nueva_prediccion["fecha"]

    guardar_estadisticas(estadisticas)


def obtener_resumen_estadisticas():
    estadisticas = cargar_estadisticas()

    return {
        "total_por_categoria": estadisticas.get("conteo_categorias", {}),
        "ultimas_5_predicciones": estadisticas.get("predicciones", [])[-5:],
        "fecha_ultima_prediccion": estadisticas.get("ultima_prediccion")
    }


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predecir", methods=["POST"])
def predecir():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        edad = float(data.get("edad"))
        fiebre = float(data.get("fiebre"))
        dolor = float(data.get("dolor"))
        dias_sintomas = float(data.get("dias_sintomas"))

        entradas = {
            "edad": edad,
            "fiebre": fiebre,
            "dolor": dolor,
            "dias_sintomas": dias_sintomas,
        }

        resultado = predecir_estado(
            edad=edad,
            fiebre=fiebre,
            dolor=dolor,
            dias_sintomas=dias_sintomas,
        )

        registrar_prediccion(resultado, entradas)

        if request.is_json:
            return jsonify({
                "estado_predicho": resultado,
                "entradas": entradas
            })

        return render_template(
            "index.html",
            resultado=resultado,
            edad=edad,
            fiebre=fiebre,
            dolor=dolor,
            dias_sintomas=dias_sintomas,
        )

    except Exception as e:
        mensaje_error = f"Error en la predicción: {str(e)}"
        if request.is_json:
            return jsonify({"error": mensaje_error}), 400
        return render_template("index.html", error=mensaje_error), 400


@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return jsonify(obtener_resumen_estadisticas())


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
