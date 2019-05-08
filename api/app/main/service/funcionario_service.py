"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.funcionario import Funcionario

def save_new_funcionario(data):
    funcionario = Funcionario(
        nome=data['nome'],
        email=data['email'],
        senha=data['senha']
        )
    save_changes(funcionario)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_all_funcionarios():
    return Funcionario.query.all()

def get_a_funcionario(id):
    return Funcionario.query.filter_by(id=id).first()