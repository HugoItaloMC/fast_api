import json
from datetime import date, datetime
from typing import *
from utils.helper import format_date_str as to_str

class JsonLabel:
    """
      Objeto para salvar dados de acesso e requisicões de usuário
    em padrão JSON
    """
    def __init__(self: object, ordem: str, user: str) -> None:
        """
          Construtor do Objeto
        :param ordem: Recebe qual secão o usuário se encontra no sistema Ex: (cadastro, login)
        :param user: Nome do usuário
        """
        self.__ordem: str = ordem
        self.__user: Optional[str] = user

    def __iter__(self):
        """
         Serializacão de objeto no Padrão JSON, via método de classe
        :return: Generator Function
        """

         yield from {
             "ordem": self.__ordem,
             "usuário": self.__user
         }

    def __str__(self):
        """
          Passando serializacão da string do Objeto
        :param self: instância de objeto
        :return: String do objeto serializado para JSON
        """
            return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
            return self.__str__()

    def to_json(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        """
         Deserializa objetos do com padrão JSON
        :param json_dct: Recebe um json
        :return: um json deserializado
        """
        return JsonLabel(json_dct['ordem'],
                         json_dct['usuário'])
class JsonCollection:

    def __init__(self: object, bbox: object) -> None:
        """
          Objeto para Aninhar Json`s
        :param bbox:   Atributo de instância para receber um objeto do tipo dict,
                     Ex: it_json = {"name_label": [json1, json2]}
        """
        self.__bbox: object = bbox
        self.__date: str = to_str(datetime.today())