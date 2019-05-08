"""
Descrição deste arquivo: aqui é criado o modelo de Aluno, que é apenas uma
classe herdeira do objeto db.Model
"""

from app.main import db


class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    CPF = db.Column(db.Integer, unique=True, nullable=False)
    matricula = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(32), unique=False, nullable=False)
    horas_de_voo = db.Column(db.Float, unique=False, nullable=False)
    aulas_supervisionadas = db.relationship('Aula_supervisionada', backref='aluno', lazy=True)

    def __repr__(self):
        return '<Aluno %r>' % self.nome