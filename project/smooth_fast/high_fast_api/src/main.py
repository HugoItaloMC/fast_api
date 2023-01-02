from sqlalchemy.orm import Session

from infra.sqlalchemy.config.database import get_db, criar_db
from schemas import schemas
from infra.sqlalchemy.repository.repository_produto import RepositorioProduto

from fastapi import FastAPI, Depends, status
from typing import *

# Criar banco de dados
# criar_db()

app = FastAPI()


@app.post('/produto', status_code=status.HTTP_201_CREATED, response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    # Criando Novos Usuários
    return RepositorioProduto(db).criar(produto)


@app.get('/produto', status_code=status.HTTP_200_OK, response_model=List[schemas.ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    # Listando Todos Usuários
    return RepositorioProduto(db).listar()

@app.post('/usuario', status_code=status.HTTP_201_CREATED, response_model=schemas.Usuario)
def criar_usuario(db: Session=Depends(get_db)):
    # Criando Usuários
    return RepositorioProduto(db).criar()