"""
Descrição do arquivo: aqui são criadas as rotas da entidade Instrutor, assim como o
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

# importar métodos de Instrutor em instrutor_service
from ..service.instrutor_service import save_new_instrutor, get_all_instrutores, get_a_instrutor


class InstrutorDto:
    api = Namespace(
        'instrutor', description='operações relacionadas a Instrutor')
    instrutor = api.model('Instrutor', {
        'id': fields.Integer,
        'nome': fields.String,
        'CPF': fields.Integer,
        'matricula': fields.Integer,
        'email': fields.String,
        'senha': fields.String,
        'horas_de_voo': fields.Float,
        'breve': fields.Integer,
        'certificado_instrutor': fields.Integer
    })


api = InstrutorDto.api
_instrutor = InstrutorDto.instrutor


@api.route('/')
class InstrutorList(Resource):
    @api.doc('Lista todos os instrutores registrados')
    @api.marshal_with(_instrutor)
    def get(self):
        """List all registered instrutores"""
        return get_all_instrutores()

    @api.response(201, 'Instrutor successfully registered.')
    @api.doc('Create a new instrutor')
    @api.expect(_instrutor)
    def post(self):
        """Creates a new instrutor"""
        data = request.json
        save_new_instrutor(data=data)
