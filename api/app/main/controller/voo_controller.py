"""
Descrição do arquivo: aqui são criadas as rotas da entidade Voo, assim como o
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
from ..service.voo_service import save_new_voo, get_all_voos, get_a_voo

class VooDto:
    api = Namespace('voo', description='operacoes relacionadas ao voo')
    voo = api.model('Voo', {
        'id': fields.Integer,
        'data_hora_inicio': fields.DateTime,
        'data_hora_fim': fields.DateTime,
        'matricula_da_aeronave': fields.String,
        'origem': fields.String,
        'destino': fields.String,
        'piloto_id': fields.Integer,
        'instrutor_id': fields.Integer
    })

api = VooDto.api
_voo = VooDto.voo
@api.route('/')
class VooList(Resource):
    @api.doc('Lista todos os voos registrados')
    @api.marshal_with(_voo)
    def get(self):
        """Lista todos os voos registrados"""
        return get_all_voos()
        
    @api.response(201, 'Voo registrado com sucesso.')
    @api.doc('Cria um novo voo')
    @api.expect(_voo)
    def post(self):
        """Cria um novo voo"""
        data = request.json
        save_new_voo(data=data)
