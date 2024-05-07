from fastapi import FastAPI


app = FastAPI()

usuarios = [(1, 'Guilherme Montenegro', 'minhasenha1'), (2, 'Andressa Borges', 'minhasenha2')]


@app.get('/usuarios/{id}')
def main(id:int):
    for usuario in usuarios:
        if usuario[0] == id:
            return usuario
    
    return 'Esse usuário não existe'