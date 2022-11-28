from typing import List, Any
from fastapi import FastAPI
from pydantic import BaseModel

"""
  Enviar parametros, tanto pela URL (end-point) quanto por método POST
a nossa Fast API
 Para visualizarmos  nossos  métodos  POST  na  nossa  API  utilizamos 
programacão ou uma interface pré-implementada do próprio framework, pa-
ra acessarmos essa interface passamos na URL o end-point '/docs'
"""

app = FastAPI()


@app.get("/test{getting}")
def main(getting: (int | float) | str) -> dict[str, (int | float) | str]:
    return {"valor": getting}


usuarios: List[tuple] = [(1, 'Gabriel', 'minhasenha1'), (2, 'Marcos', 'minhasenha2')]


@app.get("/usuario/{id}")
def user_get(id: int) -> Any:
    """
     Retorna usuário pela chave `ID`
    :param id: ID do usuário
    :return: Usuário requisitado no end-point
    """
    for i in usuarios:
        return i if i[0] == id else f"ID {id} Not Found"


# Requisicões do tipo `POST` ñ é uma requisicão atravez da URL
@app.post("/usuario")
def user_post(name: str) -> Any:
    """
     Retorna um usuário pela chave `name`
    :param name: parametro de entrada com nome do usuário
    :return: Usuário requisitado
    """
    for line in usuarios:
        return line if line[1] == name else f"User Name {name} Not Found"
