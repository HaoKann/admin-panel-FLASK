from app import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.Integer())
    email = db.Column(db.String(255))
    
    orders = db.relationship('Order', backref='client', lazy='dynamic') 

    def __repr__(self):
        return f'Клиент {self.id}, {self.name}, {self.phone_number}, {self.email}'
