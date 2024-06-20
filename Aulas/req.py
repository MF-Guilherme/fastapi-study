import requests

retorno = requests.post(f"http://127.0.0.1:8000/cadastrar_usuario", params={"id": 4, "nome": "roberta", "senha": "minhasenha4"})

print(retorno.json())