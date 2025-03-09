from app import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer(), primary_key=True)
    sup_name = db.Column(db.String(255),  nullable=False)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)

    products = db.relationship('Product', backref='supplier', lazy='dynamic')

    def __repr__(self):
        return f'Поставщик: {self.id}, {self.sup_name}, {self.address}, {self.phone_number}'