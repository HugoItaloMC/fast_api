from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path
from pydantic import BaseModel
from uuid import uuid4
from typing import *

app = FastAPI()


# Configurando CORS
# CORS serve para podermos consumirmos há API em outro host
origins = ['127.0.0.1:40166']  # Local FRONTEND

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


# Gerando schema


class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str
    peso: int


base: List[Animal] = []

# Recuperacão Geral


@app.get('/animais')
def listar_animais():
    return base


# Recuperacão unitária

@app.get('/animais/{id_animal}')
def obter_animal(animal_id: int):
    for line in base:
        if line.id == animal_id:
            return line
    return {"msg": "Animal ñ Localizado"}


# Exclusão


@app.delete('/animais/{animal_id}')
def deletar_animal(animal_id: str = Path(..., title="ID Animal Cadastrado")):
    posicao: int = -1

    # Buscar posicão usuário
    for index, value in enumerate(base):
        if value.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        base.pop(posicao)
        return {"msg": "Remocão efeturada com sucesso !"}
    else:
        return {"error": "ID não encontrado"}


# Instânciando 


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    base.append(animal)
    return {"msg": "Animal Cadastrado com sucesso"}
