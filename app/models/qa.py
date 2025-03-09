from app import db

class Qa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    response = db.Column(db.Text, nullable=False)
