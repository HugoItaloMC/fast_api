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
