# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar primero `requirements.txt`
COPY requirements.txt .

# Instalar dependencias antes de copiar todo el código
RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

# Luego, copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto donde correrá la API
EXPOSE 8000

# Comando para iniciar la API con Uvicorn
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
