from sqlalchemy.orm import Session

class RepositorioBase():

     # Instânciando Sessão
    def __init__(self, db: Session):
        self.db = db