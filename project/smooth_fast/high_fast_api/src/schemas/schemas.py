from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):

    ID: Optional[int] = None
    nome: str
    descricao: str
    disponivel: bool
    tamanho: str

    class Config:
        # Configurando nosso objeto para reconhecimento do ORM
        orm_mode = True

"""
  Client vê nosso objeto dessa forma, aqui é representado nosso objeto da camada models para o client,
as instâncias serão a partir dos objetos declarados em schemas aos nossos models
"""
