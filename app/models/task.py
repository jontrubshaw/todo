from app import db
from datetime import datetime

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	title = db.Column(db.String(140))
	description = db.Column(db.String(400))
	priority = db.Column(db.String(10))
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	reminder = db.Column(db.DateTime)

	def __repr__(self):
		return '<Task {}>'.format(self.title)