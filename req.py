import requests

retorno = requests.get("http://127.0.0.1:8000/login")

print(retorno.json()['mensagem'])