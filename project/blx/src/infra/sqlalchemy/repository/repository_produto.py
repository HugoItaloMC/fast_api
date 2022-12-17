from .main import RepositorioBase
from schemas import schemas
from infra.sqlalchemy.models import models
class RepositorioProduto(RepositorioBase):

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            disponivel=produto.disponivel,
            tamanho=produto.tamanho
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos
