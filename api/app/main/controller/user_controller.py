"""
Descrição do arquivo: aqui são criadas as rotas da entidade User, assim como o
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

# importar métodos de User em user_service
from ..service.user_service import save_new_user, get_all_users, get_a_user

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('User', {
        'id': fields.Integer,
        'username': fields.String,
        'email': fields.String
    })

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('List all registered users')
    @api.marshal_with(_user)
    def get(self):
        """List all registered users"""
        return get_all_users()
        
    @api.response(201, 'User successfully registered.')
    @api.doc('Create a new user')
    @api.expect(_user)
    def post(self):
        """Creates a new user"""
        data = request.json
        save_new_user(data=data)
