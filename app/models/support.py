from app import db
from datetime import datetime

class Support(db.Model):
    __tablename__ = 'support'

    id = db.Column(db.Integer(), primary_key=True)
    type_of_question = db.Column(db.String(255), nullable=False)
    question = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(255))
    email_for_reply = db.Column(db.String(255), nullable=False)
    date_of_appeal = db.Column(db.DateTime, default=datetime.utcnow)
    processed_or_not = db.Column(db.Boolean, default=False)
    
    respond = db.Column(db.Text, nullable=True)
    date_of_respond = db.Column(db.DateTime)
    