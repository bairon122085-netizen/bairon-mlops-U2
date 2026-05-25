from flask import Flask, jsonify, render_template, request
from modelo import predecir_estado

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predecir", methods=["POST"])
def predecir():
    """
    Permite predecir usando dos formas:
    1. Formulario web HTML.
    2. JSON vía API REST.

    Ejemplo JSON:
    {
      "edad": 35,
      "fiebre": 38.2,
      "dolor": 4,
      "dias_sintomas": 3
    }
    """
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        edad = float(data.get("edad"))
        fiebre = float(data.get("fiebre"))
        dolor = float(data.get("dolor"))
        dias_sintomas = float(data.get("dias_sintomas"))

        resultado = predecir_estado(
            edad=edad,
            fiebre=fiebre,
            dolor=dolor,
            dias_sintomas=dias_sintomas,
        )

        if request.is_json:
            return jsonify({
                "estado_predicho": resultado,
                "entradas": {
                    "edad": edad,
                    "fiebre": fiebre,
                    "dolor": dolor,
                    "dias_sintomas": dias_sintomas,
                }
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


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
