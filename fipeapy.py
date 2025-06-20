import requests

BASE_URL= "https://parallelum.com.br/fipe/api/v1/carros"

def get_marcas():

    response = requests.get(f"{BASE_URL}/marcas")
    return response.json()

def get_modelos(marca_id):
    response = requests.get(f"{BASE_URL}/marcas/{marca_id}/modelos")
    return response.json()

def get_anos(marca_id, modelo_id):
    response = requests.get(f"{BASE_URL}/marcas/{marca_id}/modelos/{modelo_id}/anos")
    return response.json()

def get_detalhes (marca_id, modelo_id, ano_id):
    response = requests.get(f"{BASE_URL}/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_id}")
    return response.json()