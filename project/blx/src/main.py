from sqlalchemy.orm import Session

from infra.sqlalchemy.config.database import get_db, criar_db
from schemas import schemas
from infra.sqlalchemy.repository.repository_produto import RepositorioProduto

from fastapi import FastAPI, Depends
from typing import *

# Criar banco de dados
criar_db()

app = FastAPI()

@app.post('/produto', response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    return RepositorioProduto(db).criar(produto)


@app.get('/produto', response_model=List[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    return RepositorioProduto(db).listar()