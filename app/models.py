from app import db

class User(db.Model):
	uid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), index=True, unique=True)
	age = db.Column(db.Integer)
	password = db.Column(db.String(20))

	def __repr__(self):
		return '<User %r>' % (self.username)

