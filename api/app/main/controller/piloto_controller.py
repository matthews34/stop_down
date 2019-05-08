"""
Descrição do arquivo: aqui são criadas as rotas da entidade Piloto, assim como o
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
from ..service.piloto_service import save_new_piloto, get_all_pilotos, get_a_piloto

class PilotoDto:
    api = Namespace('piloto', description='operacoes relacionadas ao piloto')
    piloto = api.model('Piloto', {
        'id': fields.Integer,
        'nome': fields.String,
        'cpf': fields.Integer,
        'matricula': fields.Integer,
        'email': fields.String,
        'senha': fields.String,
        'horas_de_voo': fields.Float,
        'breve': fields.Integer
    })

api = PilotoDto.api
_piloto = PilotoDto.piloto
@api.route('/')
class PilotoList(Resource):
    @api.doc('Lista todos os pilotos registrados')
    @api.marshal_with(_piloto)
    def get(self):
        """Lista todos os pilotos registrados"""
        return get_all_pilotos()
        
    @api.response(201, 'Piloto registrado com sucesso.')
    @api.doc('Cria um novo piloto')
    @api.expect(_piloto)
    def post(self):
        """Cria um novo piloto"""
        data = request.json
        save_new_piloto(data=data)
