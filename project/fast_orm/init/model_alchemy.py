from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
SENHA = 'Acesso93#'
HOST = 'localhost'
BANK = 'fast_learn'
PORT = '3306'

# Informando Para o ORM (SQLAlchemy):
# ->  SGBD a ser utilizado: 'mysql'
# -> Motor da linguagem para trabalhar com SGBD utilizado: 'pymysql'
# -> USER: Usuário em nosso cas o 'root'
# - > PASSWORD: Senha de acesso do usuário
# -> HOST: Local de Hospedagem de SGBD, em nosso caso: localhost
# -> BANK: Nome do Banco de Dados
# -> PORT: Porta em que o servidor com SGBD encontra hospedado, por pedrão MySQL vem hospedado na porta: 3306

CONN = f"mysql+pymysql://{USER}:{SENHA}@{HOST}:{PORT}/{BANK}"  # string de conexão

# Para se conectar com o DB
engine = create_engine(CONN, echo=True)  # echo=True vai me printar informacões conforme manegamos o banco

# Criando sessão
Session = sessionmaker(bind=engine)
session = Session()

# Declarando objeto para criacão de tabelas
Base = declarative_base()

"""
  Como case de estudo, iremos implementar um sistema de login
criando, autenticando, atualizando e deletando um usuário.
"""


class Pessoa(Base):

    """
    MySQL Sintax ->
    CREATE TABLE `Pessoa` (
id INTEGER NOT NULL AUTO_INCREMENT,
name VARCHAR(50),
user VARCHAR(15),
password VARCHAR(12),
PRIMARY KEY (id)
)
    """

    # SQLAchemy Syntax
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    usuario = Column(String(15))
    senha = Column(String(12))


class Tokens(Base):

    # Quando trabalhamos com autenticacão com API`s enviamos o usuário, o tempo de acesso, um token e o tempo de duracão

    """
    Mysql Syntax ->
    CREATE TABLE `Tokens` (
id INTEGER NOT NULL AUTO_INCREMENT,
id_pessoa INTEGER,
token VARCHAR(100),
date DATETIME,
PRIMARY KEY (id),
FOREIGN KEY(id_pessoa) REFERENCES `Pessoa` (id)
    )
    """

    # SQLAchemy Syntax
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))
    date = Column(DateTime, default=datetime.utcnow())


Base.metadata.create_all(engine)
