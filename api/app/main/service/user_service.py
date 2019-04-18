"""
Descrição deste arquivo: aqui são definidos os métodos a serem
usados pelas rotas do controller
"""

from app.main import db
from app.main.model.user import User

def save_new_user(data):
    user = User(
        username=data['username'],
        email=data['email']
        )
    save_changes(user)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def get_all_users():
    return User.query.all()

def get_a_user(id):
    return User.query.filter_by(id=id).first()