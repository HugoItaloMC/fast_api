from fastapi import FastAPI
from typing import Dict
"""
  Para rodarmos nossa API utilizamos um servidor para desenvolvimento (uvicorn), veja como utilizar o mesmo:
      NO TERMINAL DIGITE:
      $   nome_do_arquivo:aplicacao_api --reload
          : Passamos o parâmetro `--reload` para recarregar a cada modificacão 
"""

# Instânciando nosso objeto do tipo fastapi para aplicar métodos de requisicões, Ex:  ` aplicacão = FastAPI() `
# Por convencão nomeados nosso objeto do tipo FastAPI como `app`
app = FastAPI()

# Em API`s utilizamos URL`s para aplicar nossos métodos, essas URL`s são chamadas de end-point's.
# Para aplicar nossos métodos em nossos end-point`s, passamos o objeto FastAPI() como um decorator em nossos métodos
# Ex: ` @aplicacao.método("end-point") ` abaixo nosso método


# APLICANDO
@app.get("/")  # URL raiz
def root() -> Dict[str, str]:
    """Aplicar método na URL (end-point) '/' """
    x: int = 10
    for i in range(x):
        x += 1
    return {"mensagem": "Root point", "Valur": x}


@app.get("/cadastro")  # URL cadastro
def sign_up() -> Dict[str, str]:
    """Aplicar método na URL (end-point) '/cadastro' """
    return {"mensagem": "Sign'up"}


@app.get("/login")  # URL login
def login() -> Dict[str, str]:
    """Aplicar método na URL (end-point) '/login' """
    return {"mensagem": "login"}


@app.get("/body")  # URL body
def contents() -> Dict[str, str]:
    """Aplicar método na URL (end-point) '/body' """
    return {"mensagem": "contents"}
