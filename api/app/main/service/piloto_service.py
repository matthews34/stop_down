"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.piloto import Piloto

def save_new_piloto(data):
    piloto = Piloto(
        nome=data['nome'],
        cpf=data['cpf'],
        matricula=data['matricula'],
        email=data['email'],
        senha=data['senha'],
        horas_de_voo=data['horas_de_voo'],
        breve=data['breve']
        )
    save_changes(piloto)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_all_pilotos():
    return Piloto.query.all()

def get_a_piloto(id):
    return Piloto.query.filter_by(id=id).first()