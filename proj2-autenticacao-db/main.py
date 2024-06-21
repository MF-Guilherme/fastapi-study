from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN, Pessoa, Tokens
from secrets import token_hex


app = FastAPI()


def conecta_banco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


@app.post('/cadastro')
def cadastro(nome: str, user: str, senha: str):
    session = conecta_banco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    if len(usuario) == 0:
        x = Pessoa(nome=nome, usuario=user, senha=senha)
        session.add(x)
        session.commit()
        return {'status': 'sucesso'}
    elif len(usuario) > 0:
        return {'status': 'Usuário já cadastrado'}


@app.post('/login')
def login(usuario: str, senha: str):
    session = conecta_banco()
    user = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
    if len(user) == 0:
        return {'status': 'Usuário inexistente'}

    while True:
        token = token_hex(50)
        token_exists = session.query(Tokens).filter_by(token=token).all()
        if len(token_exists) == 0:
            pessoa_exists = session.query(Tokens).filter_by(id_pessoa=user[0].id).all()
            if len(pessoa_exists) == 0:
                novo_token = Tokens(id_pessoa=user[0].id, token=token)
                session.add(novo_token)
            elif len(pessoa_exists) > 0:
                pessoa_exists[0].token = token
            session.commit()
            break
    return token
