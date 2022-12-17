from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean

class Produto(Base):

    __tablename__ = 'Produto'

    ID = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    descricao = Column(String(100))
    disponivel = Column(Boolean)
    tamanho = Column(String(1))


