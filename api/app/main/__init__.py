"""
Este é um arquivo __init__.py, ele serve para que o python identifique que esta pasta é um módulo
Descrição: aqui é que é definido o objeto db e a função create_app() que seta inicializa o app e
seta o banco de dados
Imports deste arquivo:
    SQLAlchemy: método responsável por criar e configurar a conexão do banco de dados com o Flask
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    # criação do app
    app = Flask(__name__)
    CORS(app, origins='*')
    # configuração da conexão com o banco de dados
    # a URI segue o seguinte formato:
    # driver://username:password@host[:port]/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stopdown:semtempoirmao@localhost/stopdown'
    db.init_app(app)
    return app