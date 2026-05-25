# Servicio Docker para predicción de estado de enfermedad

## 1. Objetivo de la solución

Este proyecto implementa una solución local usando Docker para simular un servicio de predicción médica. El servicio permite que un médico ingrese datos básicos de un paciente y reciba como respuesta uno de los siguientes estados:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA

El objetivo académico es demostrar cómo empaquetar una solución de machine learning o una función predictiva simulada dentro de una imagen personalizada de Docker.

> Nota: La función incluida no corresponde a un modelo médico real. Es una simulación académica basada en reglas simples.

---

## 2. Estructura del proyecto

```text
mlops_enfermedades_docker/
├── app/
│   ├── app.py
│   ├── modelo.py
│   └── templates/
│       └── index.html
├── docs/
│   └── pipeline_mlops.md
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 3. Variables de entrada

El servicio recibe cuatro valores:

| Variable | Descripción | Ejemplo |
|---|---|---|
| edad | Edad del paciente | 35 |
| fiebre | Temperatura corporal en grados Celsius | 38.2 |
| dolor | Nivel de dolor entre 0 y 10 | 4 |
| dias_sintomas | Número de días con síntomas | 3 |

Aunque la tarea pedía al menos tres valores de entrada, se usan cuatro para que la simulación sea más clara.

---

## 4. Construir la imagen Docker

Desde la carpeta raíz del proyecto, ejecutar:

```bash
docker build -t predictor-enfermedades:1.0 .
```

---

## 5. Correr el contenedor

```bash
docker run -p 5000:5000 predictor-enfermedades:1.0
```

Después de ejecutar el comando, abrir en el navegador:

```text
http://localhost:5000
```

---

## 6. Uso mediante página web

1. Abrir `http://localhost:5000`.
2. Ingresar edad, fiebre, nivel de dolor y días con síntomas.
3. Presionar el botón **Predecir estado**.
4. La aplicación mostrará uno de los cuatro estados definidos.

---

## 7. Uso mediante API REST

También se puede consumir el servicio con `curl`:

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{"edad": 35, "fiebre": 38.2, "dolor": 4, "dias_sintomas": 3}'
```

Respuesta esperada:

```json
{
  "estado_predicho": "ENFERMEDAD LEVE",
  "entradas": {
    "edad": 35.0,
    "fiebre": 38.2,
    "dolor": 4.0,
    "dias_sintomas": 3.0
  }
}
```

---

## 8. Ejemplos para obtener todas las clases

### NO ENFERMO

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{"edad": 25, "fiebre": 36.8, "dolor": 1, "dias_sintomas": 1}'
```

### ENFERMEDAD LEVE

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{"edad": 35, "fiebre": 38.0, "dolor": 4, "dias_sintomas": 3}'
```

### ENFERMEDAD AGUDA

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{"edad": 45, "fiebre": 39.5, "dolor": 8, "dias_sintomas": 4}'
```

### ENFERMEDAD CRÓNICA

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d '{"edad": 70, "fiebre": 37.8, "dolor": 6, "dias_sintomas": 40}'
```

---

## 9. Verificación del estado del servicio

```bash
curl http://localhost:5000/health
```

Respuesta esperada:

```json
{"status": "ok"}
```

---

## 10. Detener el contenedor

Listar contenedores activos:

```bash
docker ps
```

Detener el contenedor:

```bash
docker stop <container_id>
```
