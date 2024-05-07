from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Usuario(BaseModel):
    id: int
    nome: str
    senha: str


usuarios = [
    Usuario(id=1, nome='Guilherme', senha='senhadoGuilherme'),
    Usuario(id=2, nome='Andressa', senha='senhadaAndressa'),
    Usuario(id=3, nome='Liz', senha='senhadaLiz'),
]


@app.get('/usuario/{id}')
def main(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
    return 'Esse usuário não existe'


@app.get('/listar_usuarios')
def listar():
    return usuarios


@app.post('/cadastrar_usuario')
def main(usuario: Usuario):
    usuarios.append(usuario)
    return 'Usuário cadastrado'
