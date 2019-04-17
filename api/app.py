from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# configura os parametros para acessar o db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stopdown:semtempoirmao@localhost/stopdown'
db = SQLAlchemy(app)
api = Api(app)

# modelo da entidade User:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# definição dos campos do modelo de User (para a documentação da API)
_user = api.model('User', {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# métodos de get e posts da rota users
@api.route('/users')
class UserController(Resource):
    @api.marshal_with(_user)
    def get(self):
        return User.query.all()
    @api.response(201, 'User successfully registered.')
    @api.expect(_user)
    def post(self):
        data = request.json
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)