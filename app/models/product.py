from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    prod_name = db.Column(db.String(255), nullable=False)
    prod_type = db.Column(db.String(255), nullable=False)
    prod_amount = db.Column(db.Integer(), nullable=False)
    prod_price = db.Column(db.Integer(), nullable=False)

    suppliers_id = db.Column(db.Integer(), db.ForeignKey('suppliers.id'))
    products_in_cart = db.relationship('ProductInCart', backref='product', lazy='dynamic')

    def __repr__(self):
        return f'Продукт: {self.id}, {self.prod_name}, {self.prod_type}, {self.prod_amount}'