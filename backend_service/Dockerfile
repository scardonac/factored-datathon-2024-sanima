# Descarga la imagen Base de python
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Define carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Instalar el ambiente mediante pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código al directorio de trabajo
COPY ./src ./src

# Exponer el puerto 80 para que la aplicación sea accesible
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]