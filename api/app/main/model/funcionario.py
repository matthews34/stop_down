"""
Descrição deste arquivo: aqui é criado o modelo de Funcionario, que é apenas uma
classe herdeira do objeto db.Model
"""

from app.main import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    
    id = db.Column(db.Integer, primary_key=True)
    CPF = db.Column(db.Integer, unique=True, nullable=False)
    nome = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(32), unique=False, nullable=False)

    def __repr__(self):
        return '<Funcionario %r>' % self.name