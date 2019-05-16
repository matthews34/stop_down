"""
Descrição do arquivo: aqui são criadas as rotas da entidade Aula_supervisionada, assim como o
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
from ..service.aula_supervisionada_service import save_new_aula_supervisionada, get_all_aulas_supervisionadas, get_a_aula_supervisionada

class Aula_supervisionadaDto:
    api = Namespace('aula_supervisionada', description='operacoes relacionadas a aulas supervisionadas')
    aula_supervisionada = api.model('aula_supervisionada', {
        'id': fields.Integer,
        'parecer_comentario': fields.String,
        'parecer_nota': fields.Float,
        'aluno_id': fields.Integer,
        'instrutor_id': fields.Integer,
        'voo_id': fields.Integer
    })

api = Aula_supervisionadaDto.api
_aula_supervisionada = Aula_supervisionadaDto.aula_supervisionada
@api.route('/')
class Aula_supervisionadaList(Resource):
    @api.doc('Lista todos os aulas_supervisionadas registrados')
    @api.marshal_with(_aula_supervisionada)
    def get(self):
        """Lista todos as aulas supervisionadas registrados"""
        return get_all_aulas_supervisionadas()
        
    @api.response(201, 'Aula supervisionada registrada com sucesso.')
    @api.doc('Cria uma nova aula supervisionada')
    @api.expect(_aula_supervisionada)
    def post(self):
        """Cria uma nova aula supervisionada"""
        data = request.json
        save_new_aula_supervisionada(data=data)
