from typing import Dict
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_alchemy import CONN, Pessoa, Tokens
from secrets import token_hex

# Instanciando FastAPI
app = FastAPI()



def conecta_banco():
    """
    Conexão com Banco de dados
    """
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


# Vamos criar os end-point(URL) para cadastrar usuário no banco de dados via métodos de API

# CADASTRO USUÁRIO
@app.post('/cadastro')
def cadastro(nome: str, user: str, senha: str) -> Dict[str, str]:
    """
     End-point utilizando método POST para cadastrar usuário
    :param nome: Nome Completo
    :param user: Usuário de Cadastro
    :param senha: Senha de Usuário
    :return: Dicionário com status da operacão
    """

    # Iniciando Sessão no Banco de Dados
    session = conecta_banco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    # Devemos verificar se Usuário já existe no banco
    # Criando Objeto de verificacão de existência de usuário:
    #   -> `.query(Entidade) faz a consulta` Seleciona a Tabela
    #   -> `.filter_by(atributo_entidade=atributo_instância)` Filtra consulta entre Atributos(Colunas)
    #   -> `.all()` Gera a ocorrência
    if len(usuario) == 0:
        # Instânciando a Entidade Pessoa caso usuário ñ exista
        x = Pessoa(name=nome, usuario=user, senha=senha)

        # Inserindo as Informacões no banco de dados
        session.add(x)

        # Comitando as Informacões e salvando de forma perssistente
        session.commit()
        return {"status": "Op. Sucedfull"}
    elif len(usuario) > 0:
        return {"status": "usuário já cadastrado"}


# LOGIN USUÁRIO
@app.post('/login')
def login(usuario: str, senha: str):
    """
     Funcão de login, criando um token de acesso simples no DB

    :param usuario: Usuário do DB
    :param senha: sua senha
    :return: Dict com Status da ocorrência
    """

    # Iniciando sessão no banco de dados
    session = conecta_banco()

    # Verificando se usuário e senha existe no banco de dados
    user = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
    if len(user) == 0:
        return {"status": "User not engine"}

    # Ao criarmos nosso token no login temos alguns critérios:
    # -> Ñ devemos criar redundâncias de usuários com diversos tokens
    # -> Ñ devemos repetir o token em usuários diferentes

    while True:
        token = token_hex(50)  # Objeto token_hex com seu tamanho em bytes
        # Em Hexadecimal 2 caracteres tem 1 byte
        # 50 bytes equivale a 100 caracteres que é o tamanho do nosso token declarado na tabela `Tokens`

        # Verificando se token já existe
        token_existe = session.query(Tokens).filter_by(token=token).all()
        if len(token_existe) == 0:

            # Verificando usuário já tem token e alterar apenas o token já existente
            # Se usuário ñ tiver token de acesso salvar de forma persistente usuário e seu token na tabela `Tokens`

            pessoa_existe = session.query(Tokens).filter_by(id_pessoa=user[0].id).all()
            if len(pessoa_existe) == 0:
                # Implementando caso usuário ñ tenha seu token de acesso
                novo_token = Tokens(id_pessoa=user[0].id, token=token)

                # Adicionando alteracão na sessão no banco
                session.add(novo_token)
            elif not len(pessoa_existe) == 0:
                pessoa_existe[0].token = token

            # Comitando alteracões para salvar de forma perssistente
            session.commit()
            break
    return token
