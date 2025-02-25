# 📢 API de Predicción de Ventas - FastAPI

## 📝 Descripción
Esta API permite predecir las ventas a partir del gasto en publicidad en TV, radio y periódico. Además, proporciona funcionalidades para almacenar nuevos datos en la base de datos y reentrenar el modelo de Machine Learning.

🚀 **Tecnologías utilizadas:**
- **FastAPI** - Framework para la API
- **SQLite** - Base de datos para almacenar datos de publicidad
- **Scikit-learn** - Modelo de Machine Learning
- **Joblib** - Para cargar y guardar el modelo entrenado
- **Docker** - Para contenerizar la aplicación

## 📂 Estructura del Proyecto
```
fastapi-advertaising/
│── app/
│   ├── main.py  # Código principal de la API
│── data/
│   ├── Advertising.csv  # Datos originales (si aplica)
│   ├── advertising.db   
│── models/
│   ├── advertising_model.pkl  # Modelo entrenado
│── tests/
│   ├── test_api.py  # Pruebas de la API
│── .gitignore
│── Docker-compose.yml
│── Dockerfile
│── requirements.txt
│── README.md  # Este archivo
```

---

## 📌 Endpoints de la API

### ✅ **1. Endpoint de Predicción** (`POST /predict`)
- Predice las ventas basado en los gastos en TV, radio y periódico.

**Ejemplo de solicitud:**
```json
{
    "tv": 100.0,
    "radio": 50.0,
    "newspaper": 20.0
}
```
**Ejemplo de respuesta:**
```json
{
    "ventas_predichas": 5000.75
}
```

### ✅ **2. Endpoint para Ingesta de Datos** (`POST /ingest`)
- Guarda nuevos registros en la base de datos.

**Ejemplo de solicitud:**
```json
[
    {"tv": 100, "radio": 100, "newspaper": 200, "sales": 3000},
    {"tv": 200, "radio": 230, "newspaper": 500, "sales": 4000}
]
```
**Ejemplo de respuesta:**
```json
{
    "mensaje": "Registros almacenados correctamente"
}
```

### ✅ **3. Endpoint para Reentrenamiento** (`POST /retrain`)
- Reentrena el modelo con los nuevos datos almacenados en la base de datos.

**Ejemplo de respuesta:**
```json
{
    "mensaje": "El modelo ha sido reentrenado correctamente."
}
```

### ✅ **4. Endpoint de Estado** (`GET /`)
- Comprueba si la API está funcionando.

**Ejemplo de respuesta:**
```json
{
    "mensaje": "La API del Modelo de Publicidad está funcionando"
}
```

---

## ⚙️ Instalación y Uso

### 1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/fastapi-advertaising.git
cd fastapi-advertaising
```

### 2️⃣ **Crear un entorno virtual (Opcional pero recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Ejecutar la API en local**
```bash
uvicorn app.main:app --reload
```
📌 **La API estará disponible en:** `http://localhost:8000/docs`

---

## 🐳 Ejecución con Docker

### 1️⃣ **Construir la imagen de Docker**
```bash
docker build -t fastapi-advertising .
```

### 2️⃣ **Ejecutar el contenedor**
```bash
docker run -p 8000:8000 fastapi-advertising
```

📌 **Accede a la API en:** `http://localhost:8000/docs`

---

## 🚀 Despliegue en Docker Hub

### 1️⃣ **Iniciar sesión en Docker Hub**
```bash
docker login
```

### 2️⃣ **Etiquetar la imagen**
```bash
docker tag fastapi-advertising tuusuario/fastapi-advertising:v1
```

### 3️⃣ **Subir la imagen a Docker Hub**
```bash
docker push tuusuario/fastapi-advertising:v1
```

### 4️⃣ **Ejecutar la API desde Docker Hub**
```bash
docker run -p 8000:8000 tuusuario/fastapi-advertising:v1
```

📌 **La API estará disponible en:** `http://localhost:8000/docs`

---

## 🧪 Pruebas con `pytest`

Para ejecutar las pruebas automáticas, ejecuta:
```bash
pytest tests/test_api.py
```
Si todas las pruebas pasan, verás un mensaje de confirmación.

---


