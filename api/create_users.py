from app import db, User

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
matheus = User(username='Matheus', email='matheus@example.com')
luca = User(username='Luca', email='luca@example.com')
thabata = User(username='Thabata', email='thabata@example.com')
vecchi = User(username='Vecchi', email='vecchi@example.com')
palmito = User(username='Palmito', email='palmito@example.com')

db.create_all()

db.session.add(admin)
db.session.add(guest)
db.session.add(matheus)
db.session.add(luca)
db.session.add(thabata)
db.session.add(vecchi)
db.session.add(palmito)

db.session.commit()