from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, List

"""
  pydantic.BaseModel: Cria Dados e tipos de dados em uma classe
  Por padrão FastAPI foi desenvolvido para se interagir com pydantic.BaseModel, está lib facilita na criacão do 
nossos modelos a serem instânciados.
"""

app = FastAPI()


class Usuario(BaseModel):
    """
      Objeto do tipo pydantic.BaseModel
    para criar nosso modelo para ser in-
    tânciado por nossa API
    """
    id: int
    name: str
    senha: str


lista_usuarios: List[Usuario] = [
    Usuario(id=1, name='Italo', senha='Minhasenha123'),
    Usuario(id=2, name='Correia', senha='Minhasenha321'),
    Usuario(id=3, name='Hugo', senha='Minhasenha112233')
]


@app.post('/usuario')
def cadastro(usuario: Usuario) -> str:
    """
      Funcão Para Cadastrar Usuário atráves do méotod POST
    :param usuario: Parametro de entrada obrigatório
    :return: String afirmando ocorrência da funcão
    """
    lista_usuarios.append(usuario)
    return "Sucedfull creat user"


@app.get('/listar_usuario')
def usuarios() -> List[Usuario]:
    """
    Funcão Para listar usuários através do método GET
    :return: Objeto do Tipo List[Usuario]
    """
    return lista_usuarios
