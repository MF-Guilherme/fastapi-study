import requests

retorno = requests.get(f"http://127.0.0.1:8000/usuarios/1")

print(retorno.json())