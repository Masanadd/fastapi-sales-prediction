import requests

def test_ingest_endpoint():
    url = 'http://localhost:8000/ingest'  
    data = [
    {'tv': 100, 'radio': 100, 'newspaper': 200, 'sales': 3000},
    {'tv': 200, 'radio': 230, 'newspaper': 500, 'sales': 4000}
]
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Datos ingresados correctamente'}

def test_predict_endpoint():
    url = 'http://localhost:8000/predict'  
    data = {'tv': 100, 'radio': 100, 'newspaper': 200}
    
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert 'prediction' in response.json()

def test_retrain_endpoint():
    url = 'http://localhost:8000/retrain'  
    response = requests.post(url)
    assert response.status_code == 200
    assert response.json() == {'message': 'Modelo reentrenado correctamente.'}