from app.modelo import predecir_estado


def test_no_enfermo():
    resultado = predecir_estado(
        edad=25,
        fiebre=36.5,
        dolor=1,
        dias_sintomas=1
    )

    assert resultado == "NO ENFERMO"


def test_enfermedad_aguda():
    resultado = predecir_estado(
        edad=40,
        fiebre=39,
        dolor=8,
        dias_sintomas=6
    )

    assert resultado == "ENFERMEDAD AGUDA"
