"""
Descrição do arquivo: aqui são criadas as rotas da entidade Funcionario, assim como o
DTO de usuário (idealmente os DTO's ficariam em um arquivo a parte, mas por
simplicidade faremos aqui). O DTO serve para criarmos o blueprint da entidade e
definir qual é a estrutura que se espera receber em requisições (em um POST,
por exemplo)
Imports deste arquivo:
    request: objeto que recebe as requisições feitas ao servidor
    Namespace: (da descrição oficial do objeto) o Namespace está para a API
como Bluesprint está para o Flask
    fields: campos necessários para a criação do Namespace
"""

from flask import request
from flask_restplus import Resource, Namespace, fields

# importar métodos de Funcionario em funcionario_service
from ..service.funcionario_service import save_new_funcionario, get_all_funcionarios, get_a_funcionario


class FuncionarioDto:
    api = Namespace(
        'funcionário', description='operações relacionadas a funcionário')
    funcionario = api.model('Funcionario', {
        'id': fields.Integer,
        'nome': fields.String,
        'CPF': fields.Integer,
        'email': fields.String,
        'senha': fields.String
    })


api = FuncionarioDto.api
_funcionario = FuncionarioDto.funcionario
@api.route('/')
class FuncionarioList(Resource):
    @api.doc('Lista todos os funcionarios')
    @api.marshal_with(_funcionario)
    def get(self):
        """List all registered funcionarios"""
        return get_all_funcionarios()

    @api.response(201, 'Funcionário registrado com sucesso.')
    @api.doc('Criar novo funcionário')
    @api.expect(_funcionario)
    def post(self):
        """Creates a new funcionario"""
        data = request.json
        save_new_funcionario(data=data)
