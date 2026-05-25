import requests

def consumir_gastos():
    url = "http://localhost:8080/api/v1/gastos"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()

def consumir_usuarios():
    url = "http://localhost:8080/api/v1/usuarios"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()
