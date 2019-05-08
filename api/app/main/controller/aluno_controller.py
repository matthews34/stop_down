"""
Descrição do arquivo: aqui são criadas as rotas da entidade Aluno, assim como o
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

# importar métodos de Aluno em aluno_service
from ..service.aluno_service import save_new_aluno, get_all_alunos, get_a_aluno


class AlunoDto:
    api = Namespace(
        'aluno', description='operações relacionadas a Aluno')
    Aluno = api.model('Aluno', {
        'id': fields.Integer,
        'nome': fields.String,
        'CPF': fields.Integer,
        'matricula': fields.Integer,
        'email': fields.String,
        'senha': fields.String,
        'horas_de_voo': fields.Float
    })


api = AlunoDto.api
_aluno = AlunoDto.Aluno


@api.route('/')
class AlunoList(Resource):
    @api.doc('Lista todos os alunos registrados')
    @api.marshal_with(_aluno)
    def get(self):
        """List all registered alunos"""
        return get_all_alunos()

    @api.response(201, 'Aluno successfully registered.')
    @api.doc('Create a new Aluno')
    @api.expect(_aluno)
    def post(self):
        """Creates a new Aluno"""
        data = request.json
        save_new_aluno(data=data)
