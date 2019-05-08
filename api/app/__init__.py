"""
Este é um arquivo __init__.py, ele serve para que o python identifique que esta pasta é um módulo
Descrição do arquivo: aqui é criado a blueprint, para a modularização do projeto, a API com
informações sobre a documentação (título e versão, é possível adicionar descrição também) e são
adicionados à API os namespaces
"""

from flask_restplus import Api
from flask import Blueprint

# importar namespace do controller
from .main.controller.instrutor_controller import api as instrutor_ns
from .main.controller.funcionario_controller import api as funcionario_ns
from .main.controller.piloto_controller import api as piloto_ns
from .main.controller.voo_controller import api as voo_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='STOP DOWN',
          version='1.0'
          )

# adicionar namespaces na API, para setar as rotas e a documentação
api.add_namespace(instrutor_ns, path='/instrutor')
api.add_namespace(funcionario_ns, path='/funcionario')
api.add_namespace(piloto_ns, path='/piloto')
api.add_namespace(voo_ns, path='/voo')