"""
Descrição deste arquivo: aqui é criado o modelo de Instrutor, que é apenas uma
classe herdeira do objeto db.Model
"""

from app.main import db


class Instrutor(db.Model):
    __tablename__ = 'instrutores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    CPF = db.Column(db.Integer, unique=True, nullable=False)
    matricula = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(32), unique=False, nullable=False)
    horas_de_voo = db.Column(db.Float, unique=False, nullable=False)
    breve = db.Column(db.Integer, unique=True, nullable=False)
    certificado_instrutor = db.Column(db.Integer, unique=True, nullable=False)
    voos = db.relationship('Voo', backref='instrutor', lazy=True)

    def __repr__(self):
        return '<Instrutor %r>' % self.nome
