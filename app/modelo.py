"""
Modelo simulado para clasificación de estado de enfermedad.

Este archivo NO entrena un modelo real. Para fines académicos,
implementa una función determinística que recibe variables clínicas
simples y retorna una de cuatro clases requeridas:
- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
"""


def predecir_estado(edad: float, fiebre: float, dolor: float, dias_sintomas: float) -> str:
    """
    Clasifica el estado del paciente a partir de 4 variables.

    Parámetros
    ----------
    edad : float
        Edad del paciente en años.
    fiebre : float
        Temperatura corporal en grados Celsius.
    dolor : float
        Intensidad del dolor en escala de 0 a 10.
    dias_sintomas : float
        Número de días con síntomas.

    Retorna
    -------
    str
        Una de las clases: NO ENFERMO, ENFERMEDAD LEVE,
        ENFERMEDAD AGUDA o ENFERMEDAD CRÓNICA.
    """

    # Validaciones mínimas
    if edad < 0 or fiebre < 30 or fiebre > 45 or dolor < 0 or dolor > 10 or dias_sintomas < 0:
        raise ValueError("Los valores ingresados están fuera de los rangos esperados.")

    # Reglas simples para simular un modelo predictivo.
    # La función puede retornar todas las clases según los parámetros.
    if fiebre < 37.5 and dolor <= 2 and dias_sintomas <= 2:
        return "NO ENFERMO"

    if dias_sintomas >= 30 or (edad >= 65 and dias_sintomas >= 15 and dolor >= 5):
        return "ENFERMEDAD CRÓNICA"

    if fiebre >= 39 or dolor >= 8 or (fiebre >= 38.5 and dias_sintomas >= 5):
        return "ENFERMEDAD AGUDA"

    return "ENFERMEDAD LEVE"
