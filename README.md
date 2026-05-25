# Proyecto MLOps Unidad 2

## Descripción General

Este proyecto corresponde a una solución académica de MLOps orientada a la predicción simulada de enfermedades en pacientes utilizando variables clínicas básicas.

La solución fue desarrollada utilizando Python, Flask, Docker y GitHub Actions, implementando buenas prácticas de:

- Control de versiones
- Desarrollo basado en ramas
- Pull Requests
- Integración continua (CI)
- Despliegue continuo (CD)
- Dockerización
- Automatización mediante GitHub Actions

---

# Objetivo del Proyecto

Construir un flujo básico de MLOps que permita:

- Gestionar el ciclo de vida del modelo mediante GitHub.
- Versionar cambios utilizando ramas y Pull Requests.
- Automatizar validaciones y pruebas unitarias.
- Construir y publicar imágenes Docker automáticamente.
- Simular un entorno empresarial de integración y despliegue continuo.

---

# Categorías de Predicción

El modelo simulado puede retornar las siguientes categorías:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
- ENFERMEDAD TERMINAL

---

# Funcionalidades Implementadas

## Predicción de enfermedades

La aplicación permite realizar predicciones a partir de:

- Edad
- Temperatura corporal
- Nivel de dolor
- Días con síntomas

---

## Estadísticas de predicciones

La solución incorpora un sistema básico de monitoreo y trazabilidad mediante:

- Número total de predicciones por categoría
- Últimas 5 predicciones realizadas
- Fecha de la última predicción

La información se almacena en:

```text
stats.json
```

---

# Endpoints Disponibles

## Página principal

```text
GET /
```

---

## Predicción

```text
POST /predecir
```

Ejemplo:

```json
{
  "edad": 90,
  "fiebre": 39,
  "dolor": 8,
  "dias_sintomas": 20
}
```

---

## Estadísticas

```text
GET /estadisticas
```

---

## Health Check

```text
GET /health
```

---

# Estructura del Proyecto

```text
.
├── app/
│   ├── app.py
│   ├── modelo.py
│   └── templates/
│       └── index.html
│
├── tests/
│   └── test_modelo.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Dockerfile
├── requirements.txt
├── stats.json
├── modelo.py
└── README.md
```

---

# Pipeline CI/CD

El proyecto implementa un pipeline automatizado mediante GitHub Actions que:

- Ejecuta pruebas unitarias automáticamente.
- Valida Pull Requests hacia `main`.
- Construye imágenes Docker automáticamente.
- Publica imágenes Docker en GitHub Container Registry (GHCR).

Eventos automatizados:

- `pull_request`
- `push`

---

# Docker

## Construcción de imagen

```bash
docker build -t bairon-mlops-u2 .
```

## Ejecución del contenedor

```bash
docker run -p 5000:5000 bairon-mlops-u2
```

---

# Registro Docker Publicado

Imagen disponible en:

```text
ghcr.io/bairon122085-netizen/bairon-mlops-u2:latest
```

---

# Tecnologías Utilizadas

- Python
- Flask
- Docker
- GitHub
- GitHub Actions
- Pytest

---

# Autor

Bairon Gutierrez
````
