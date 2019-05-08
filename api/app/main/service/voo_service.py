"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.voo import Voo

def save_new_voo(data):
    voo = Voo(
        data_hora_inicio=data['data_hora_inicio'],
        data_hora_fim=data['data_hora_fim'],
        matricula_da_aeronave=data['matricula_da_aeronave'],
        origem=data['origem'],
        destino=data['destino'],
        piloto_id=data['piloto_id'],
        instrutor_id=data['instrutor_id']
        )
    save_changes(voo)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_all_voos():
    return Voo.query.all()

def get_a_voo(id):
    return Voo.query.filter_by(id=id).first()