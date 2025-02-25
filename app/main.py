import sqlite3
import joblib
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List

app = FastAPI(
    title="API del Modelo de Publicidad",
    description="Predice ventas a partir del gasto en TV, Radio y Periódico. También permite almacenar nuevos datos y reentrenar el modelo.",
    version="1.0.0"
)

# Configuración de la base de datos
def get_db_connection():
    conn = sqlite3.connect("data/advertising.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS advertising_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tv REAL,
        radio REAL,
        newspaper REAL,
        sales REAL
    )
""")
conn.commit()
conn.close()

# Cargar el modelo preentrenado
RUTA_MODELO = "data/advertising_model.pkl"
try:
    modelo = joblib.load(RUTA_MODELO)
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="El modelo no se encuentra. Verifica la ruta.")

# Modelos de datos con Pydantic
class CaracteristicasPrediccion(BaseModel):
    tv: float
    radio: float
    newspaper: float

class RegistroIngesta(CaracteristicasPrediccion):
    sales: float

# Endpoints
@app.get("/")
def home():
    return {"mensaje": "La API del Modelo de Publicidad está funcionando"}

@app.post("/predict")
def predecir_ventas(datos: CaracteristicasPrediccion):
    caracteristicas = np.array([[datos.tv, datos.radio, datos.newspaper]])
    prediccion = modelo.predict(caracteristicas)
    return {"ventas_predichas": float(prediccion[0])}

@app.post("/ingest")
def ingresar_datos(registros: List[RegistroIngesta]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for registro in registros:
        cursor.execute("""
            INSERT INTO advertising_data (tv, radio, newspaper, sales)
            VALUES (?, ?, ?, ?)
        """, (registro.tv, registro.radio, registro.newspaper, registro.sales))
    
    conn.commit()
    conn.close()
    return {"mensaje": "Registros almacenados correctamente"}

@app.post("/retrain")
def reentrenar_modelo():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tv, radio, newspaper, sales FROM advertising_data")
    filas = cursor.fetchall()
    conn.close()
    
    if not filas:
        raise HTTPException(status_code=400, detail="No hay datos suficientes para reentrenar.")
    
    X = np.array([[fila["tv"], fila["radio"], fila["newspaper"]] for fila in filas])
    y = np.array([fila["sales"] for fila in filas])
    
    from sklearn.linear_model import LinearRegression
    nuevo_modelo = LinearRegression()
    nuevo_modelo.fit(X, y)
    joblib.dump(nuevo_modelo, RUTA_MODELO)
    
    global modelo
    modelo = nuevo_modelo
    
    return {"mensaje": "El modelo ha sido reentrenado correctamente."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
