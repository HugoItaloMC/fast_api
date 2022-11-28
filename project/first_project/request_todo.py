import requests
from datetime import datetime
from project.first_project.utils.helper import format_date_str as to_str

# instânciando Lista de Tarefas via requests

date_now: str = to_str(datetime.today())

rest: requests = requests.post("http://127.0.0.1:8000/inserir",
                               json={"tarefa": "jantar",
                                     "realizada": False,
                                     "prazo": date_now
                                     }
                               )
print(rest.json())

# Ñ passamos a propriedade `prazo` pois JSON ñ reconhece objetos Python do tipo datetime
# Para instânciar devemos implementar um métoodo transformando objeto do tipo datetime para tipo str
