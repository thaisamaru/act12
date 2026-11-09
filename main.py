from fastapi import FastAPI

# Esta linha é obrigatória para criar o 'app'
app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API funcionando!"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}
