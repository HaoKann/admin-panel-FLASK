from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer(), primary_key=True)
    order_description = db.Column(db.String(255))
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'), nullable=False)
    products = db.relationship('ProductInCart', backref='order', lazy='dynamic')

    def __repr__(self):
        return f'Заказ {self.id}, {self.order_description}, {self.order_amount}'
    


class ProductInCart(db.Model):
    __tablename__ = 'products_in_cart'

    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Integer())

    order_id = db.Column(db.Integer(), db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    

    

# for p in o.products.all():
#     print(p.product.prod_name, '-' p.amount )
    
