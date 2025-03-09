from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddProductInCart(FlaskForm):
    amount = IntegerField('Введите количество товара: ', default=1)
    product = SelectField('Товар', coerce=int)
    submit = SubmitField('Подтвердить')