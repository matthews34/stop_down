from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stopdown:semtempoirmao@localhost/stopdown'
db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

_user = api.model('User', {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/users')
class UserController(Resource):
    @api.marshal_with(_user)
    def get(self):
        return User.query.all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)