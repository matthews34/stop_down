"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.instrutor import Instrutor


def save_new_instrutor(data):
    instrutor = Instrutor(
        nome=data['nome'],
        CPF=data['CPF'],
        matricula=data['matricula'],
        email=data['email'],
        senha=data['senha'],
        horas_de_voo=data['horas_de_voo'],
        breve=data['breve'],
        certificado_instrutor=data['certificado_instrutor']
    )
    save_changes(instrutor)


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_instrutores():
    return Instrutor.query.all()


def get_a_instrutor(id):
    return Instrutor.query.filter_by(id=id).first()
