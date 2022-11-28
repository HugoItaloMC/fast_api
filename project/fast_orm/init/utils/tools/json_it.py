import json
from typing import *

class JsonLabel:
    """
      Objeto para salvar dados de acesso e requisicões de usuário
    """
    def __init__(self: object, ordem: str, user: str) -> None:
        """
          Construtor do Objeto
        :param ordem: Recebe em que ordem o usuário está Ex: (cadastro, login)
        :param user: Nome do usuário
        """
        self.__ordem: str = ordem
        self.__user: Optional[str] = user

    def __iter__(self):
         yield from {
             "ordem": self.__ordem,
             "usuário": self.__user
         }

    def __str__(self):
            return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
            return self.__str__()

    def to_json(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return JsonLabel(json_dct['ordem'],
                         json_dct['usuário'])
class NestedJson:

    def __init__(self: object, bbox: object) -> None:
        """
          Objeto para Aninhar Json`s
        :param bbox:   Atributo de instância para receber um objeto do tipo dict,
                     Ex: it_json = {"name_label": [json1, json2]}
        """
        self.__bbox: object = bbox
        self.__date: date = date