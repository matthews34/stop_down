"""
Descrição deste arquivo: aqui é criado o modelo de Aula_supervisionada, que é apenas uma
classe herdeira do objeto db.Model
"""

from app.main import db

class Aula_supervisionada(db.Model):
    __tablename__ = 'aulas_supervisionadas'
    
    id = db.Column(db.Integer, primary_key=True)
    parecer_comentario = db.Column(db.String(300), unique=False, nullable=False)
    parecer_nota = db.Column(db.Float, unique=False, nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    instrutor_id = db.Column(db.Integer, db.ForeignKey('instrutores.id'), nullable=False)
    voo_id = db.Column(db.Integer, db.ForeignKey('voo.id'), nullable=False)

    def __repr__(self):
        return '<Aula_supervisionada %r>' % self.nome