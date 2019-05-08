"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.aluno import Aluno


def save_new_aluno(data):
    aluno = Aluno(
        nome=data['nome'],
        CPF=data['CPF'],
        matricula=data['matricula'],
        email=data['email'],
        senha=data['senha'],
        horas_de_voo=data['horas_de_voo']
    )
    save_changes(aluno)


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_alunos():
    return Aluno.query.all()


def get_a_aluno(id):
    return Aluno.query.filter_by(id=id).first()
