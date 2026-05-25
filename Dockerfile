# Imagen base liviana con Python
FROM python:3.11-slim

# Evita archivos .pyc y mejora logs en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente de la aplicación
COPY app/ .

# Puerto de exposición del servicio
EXPOSE 5000

# Comando para ejecutar la aplicación en producción básica
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
