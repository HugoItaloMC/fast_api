from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app_blx.db"  # URL base de dados

# Criando nosso motor ao banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

# Sessão ao banco de dados
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def criar_db():
    # Cricão de base de dados a partir da URL

    Base.metadata.create_all(bind=engine)


def get_db():
    # Instânciando sessão

    db = session_local()
    try:
        yield db
    finally:
        # fechando sessão
        db.close()
