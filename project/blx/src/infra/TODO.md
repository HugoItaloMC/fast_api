# 

      Camada de configuracão da aplicacão e do banco de dados
     estrutura de nossas entidades conexão com o DB e mediador
     com o front-end
      Como estamos utilizando o ORM Python SqlAlchemy criamos 
     um diretório sqlalchemy e estruturamos nossas camadas a 
     partir dele.

# CONFIG
      No diretório `config` temos um arquivero `database.py`
     que contém configuracões de conexão com o nosso DB uti-
     lizando SQLAlchemy.

# MODELS
      Em models está declarado nossas entidades, podemos criar
     nossas tabelas a partir da Syntax do ORM ou mapear um DB
     já existente utilizando ORM

# REPOSITORY
       Repository é o mediador das requests e responses da nos-
      sa API, instânciando nossos models a partir dos schemas 
