from fastapi import FastAPI

"""
  Para rodarmos nossa API utilizamos um servidor para desenvolvimento, uvicorn, veja como utilizar o mesmo:
      >>> uvicorn nome_do_modulo:aplicacao_api --reload
          : Passamos o parâmetro `--reload` para recarregar a cada modificacão 

"""

app = FastAPI()

# Em API`s utilizamos URL`s para aplicar nossas funcões, essas URL`s são chamadas de end-point's

@app.get("/")  # URL raiz
def root() -> dict[str, str]:
    """Aplicar funcão na URL (end-point) '/' """
    return {"mensagem": "Root folder"}


@app.get("/cadastro")  # URL cadastro
def sign_up() -> dict[str, str]:
    """Aplicar funcão na URL (end-point) '/cadastro' """
    return {"mensagem": "Sign'up"}


@app.get("/login")  # URL login
def login() -> dict[str, str]:
    """Aplicar funcão na URL (end-point) '/login' """
    return {"mensagem": "login"}


@app.get("/body")  # URL body
def contents() -> dict[str, str]:
    """Aplicar funcão na URL (end-point) '/body' """
    return {"mensagem": "contents"}
