from .main import RepositorioBase as bs
from high_fast_api.src.schemas.schemas import Usuario as UserSchema
from high_fast_api.src.infra.sqlalchemy.models import models


class RepositorioUsuario(bs):

    def criar(self, usuario: UserSchema):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            senha=usuario.senha,
            telefone=usuario.telefone
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuario = self.db.query(models.Usuario).all()
        return usuario
