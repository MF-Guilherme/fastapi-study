import requests

retorno = requests.post(f"http://127.0.0.1:8000/usuarios", params={'nome': 'Guilherme Montenegro'})

print(retorno.json())