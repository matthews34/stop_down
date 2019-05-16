"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.aula_supervisionada import Aula_supervisionada

def save_new_aula_supervisionada(data):
    aula_supervisionada = Aula_supervisionada(
        parecer_comentario=data['parecer_comentario'],
        parecer_nota=data['parecer_nota'],
        aluno_id=data['aluno_id'],
        instrutor_id=data['instrutor_id'],
        voo_id=data['voo_id']
        )
    save_changes(aula_supervisionada)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_all_aulas_supervisionadas():
    return Aula_supervisionada.query.all()

def get_a_aula_supervisionada(id):
    return Aula_supervisionada.query.filter_by(id=id).first()