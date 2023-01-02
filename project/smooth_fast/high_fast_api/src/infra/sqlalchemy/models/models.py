# Módulo de criacão das entidades utilizando ORM (SQLAlchemy)

from high_fast_api.src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Usuario(Base):

    __tablename__ = 'Usuario'

    ID = Column(Integer,
                primary_key=True,
                index=True)

    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    produto = relationship("Produto",
                           back_populates="usuario")

class Produto(Base):

    __tablename__ = 'Produto'

    ID = Column(Integer,
                primary_key=True,
                index=True, UniqueConstraint=True)

    nome = Column(String(50))
    descricao = Column(String(100))
    disponivel = Column(Boolean)
    tamanho = Column(String(1))
    valor_produto = Column(Integer)
    quantidade = Column(Integer)

    usuario_id = Column(Integer, ForeignKey('Usuario.ID', name='fk_usuario_id'))
    usuario = relationship('Produto', back_populates="prouto")