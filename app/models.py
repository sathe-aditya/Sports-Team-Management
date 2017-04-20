from app import db

class User(db.Model):
	uid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), index=True, unique=True)
	age = db.Column(db.Integer)
	password = db.Column(db.String(20))
	userType = db.Column(db.String(20))

	def __repr__(self):
		return '<User %r>' %(self.username)

class Match(db.Model):
	mid = db.Column(db.Integer, primary_key=True)
	opponent = db.Column(db.String(30))
	date = db.Column(db.String(30))
	time = db.Column(db.String(30))

	def __repr__(self):
		return '<Match %r>' % (self.opponent)

class Player(db.Model):
	pid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	height = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	position = db.Column(db.String(30))
	jersey = db.Column(db.Integer)
	uname = db.Column(db.String(30), db.ForeignKey('user.username'))

	def __repr__(self):
		return '<Player %r>' % (self.name)