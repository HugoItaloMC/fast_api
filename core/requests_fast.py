"""
 Normalmente ñ criamos uma API para ser vista no navegador e sim para ser
consumida por qualquer  linguagem de programacão (Python, C#, Java).
"""

import requests

"""
# TEST FILE: first_api.py >>>

# GET :
# rest = requests.get("http://127.0.0.1:8000")

# Retornando textos do método no end-point raiz '/'
# print(rest.text)

# Retornando JSON do método no end-point raiz '/'
# print(rest.json())

# Podemos recuperar informacões pelas chaves do end-point raiz '/'
# print(rest.json()["mensagem"])
# print(rest.json()["Valur"])


# TEST FILE: getting_inputs.py >>> 

# MÉTODO POST :
# 
#  usuarios: List[tuple] = [(1, 'Gabriel', 'minhasenha1'), (2, 'Marcos', 'minhasenha2')]
rest = requests.post("http://127.0.0.1:8000/usuario", params={"name": "Gabriel"})

# Retornando JSON do método no end-point '/usuario'
print(rest.json())
"""

# Tests File pydantic_fast.py >>>

# POST
#  Cadastrando novos usuários através do método POST:
# Requisicões atrávés do método POST como propriedade de instância no lugar de `params=` passamos a propriedade `json=`
rest = requests.post("http://127.0.0.1:8000/usuario", json={"id": 3, "name": "Gabriel", "senha": "senha4321"})
print(rest.json())
