from app import db
import datetime

class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Model(db.Integer(), primary_key=True)
    bill_number = db.Model(db.Integer())
    date_of_bill = db.Column(db.DateTime(), default=datetime.utcnow)

    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'))

    def __repr__(self):
        return f'Счет {self.id}, {self.bill_number}, {self.date_of_bill}'

