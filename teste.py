from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    n = 10
    for i in range(10):
        n += 1

    return {'mensagem': 'Home', 'valor': n}


@app.get('/login')
def root():
    return {'mensagem': 'Login'}


@app.get('/cadastro')
def root():
    return {'mensagem': 'Cadastro'}

