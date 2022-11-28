"""
  Neste projeto iremos implementar uma lista de tarefas do inglês `TODO-LIST`
lista de afazeres.
"""

from fastapi import FastAPI
from typing import List, Dict
from project.first_project.models.models_todo import Todo

app = FastAPI()


# Simulando Banco de Dados em uma lista, cada elemento da lista contém uma instância de `Todo`
lista_tarefas: List[Todo] = []


# Instânciando lista_tarefas


@app.post("/inserir")
def insert(todo: Todo) -> Dict[str, str]:
    """
      Funcão para inserir novas insâncias a lista_tarefas
    :param todo: Parametro de entrada para instânciar lista_tarefa
    :return: status da ocorrência da funcão insert()
    """
    # Tratando erros
    try:
        lista_tarefas.append(todo)
        return {"status": "Request Sucedfull"}
    except Exception as err:
        return {"status": f"Error ## \t>>> {err}"}


@app.post("/listar")
def listar_todo(opcao: int = 0) -> List[Todo] | Dict[str, str]:
    """
     Listar tarefas geral
    :param opcao: Parametro de entrada para retornar tarefas executadas ou ñ
    :return: lista_tarefas realizadas conforme opcao
    """
    try:
        if opcao == 0:
            # Retornando toda lista de tarefas
            return lista_tarefas
        elif opcao == 1:
            # Retornandn listas com tarefas Ñ realizadas
            return list(filter(lambda x: not False != x.realizada, lista_tarefas))
        elif opcao == 2:
            # Retornando lista com tarefas realizadas
            return list(filter(lambda x: not x.realizada != True, lista_tarefas))
    except Exception as err:
        return {"status": f"Error ##\t>>> {err}"}


@app.get("/tarefa/{id}")
def first_list_todo(id: int) -> Todo | Dict[str, str]:
    """
     Funcão para retornar tarefas por unidade
    :param id: Posicão/Indice do objeto lista_tarefas
    :return: lista_tarefas na posicão passada no id | status da ocorrência da funcão
    """
    try:
        # Retornando lista pelo indice/posicão da lista_tarefas
        return lista_tarefas[id]
    except Exception as err:
        return {"status": f"Error >>> {err}"}


@app.post('/alter')
def altera_status(id: int) -> Dict[str, str]:
    """
     Altera valores armazenador em lista_tarefas
    :param id: Parametro de entrada obrigatório, ID da tarefa
    :return: Mensagem de status da ocorrência
    """
    try:
        lista_tarefas[id].realizada = not lista_tarefas[id].realizada
        return {"status": "Order Sucedfull"}
    except Exception as err:
        return {"status": f"Error ## >>>{err}"}


@app.post('/delete')
def excluse(id: int) -> Dict[str, str]:
    try:
        del lista_tarefas[id]
        return {"status": "Op. Sucedfull"}
    except Exception as err:
        return {"status": f"Error ## >>> {err}"}
