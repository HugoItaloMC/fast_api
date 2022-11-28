from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    """
     Lista de Tarefas
    """
    tarefa: str
    realizada: bool
    prazo: Optional[str]


