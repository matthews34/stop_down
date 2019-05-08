"""
Descrição deste arquivo: aqui é criado o modelo de Voo, que é apenas uma
classe herdeira do objeto db.Model
"""

from app.main import db

class Voo(db.Model):
    __tablename__ = 'voos'
    
    id = db.Column(db.Integer, primary_key=True)
    data_hora_inicio = db.Column(db.DateTime, unique=False, nullable=False)
    data_hora_fim = db.Column(db.DateTime, unique=False, nullable=False)
    matricula_da_aeronave = db.Column(db.String(40), unique=True, nullable=False)
    origem = db.Column(db.String(200), unique=False, nullable=False)
    destino = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return '<Voo %r>' % self.id