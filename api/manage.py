"""
Descrição do arquivo: este é o arquivo principal da API, aqui será feito o gerenciamento do banco de dados
(com os comandos drop_db e create_db, por exemplo) e a execução da API (com o comando run)
Imports deste arquivo:
    Manager: permite criar comandos para usar na linha de comando com o decorator @manager.command
    create_app: cria o app já com o db setado (ver em app/main/__init__.py)
    db: objeto SQAlchemy para o gerenciamento do banco de dados através do Flask
    blueprint: objeto que registra informações a respeito das funções da API (útil para a modularização)
"""

from flask_script import Manager
from app.main import create_app, db
from app import blueprint

app = create_app()
app.register_blueprint(blueprint)

# liga o contexto do 'app' ao contexto atual do script
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    """Run the API"""
    app.run(debug=True, host='0.0.0.0', port=5000)

@manager.command
def drop_db():
    """Drop the database removing all its contents"""
    db.drop_all()

@manager.command
def create_db():
    """Create the database"""
    db.create_all()

if __name__ == '__main__':
    manager.run()