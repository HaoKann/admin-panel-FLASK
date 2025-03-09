from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models.suppliers import Supplier


class ProdForm(FlaskForm):
    prod_name = StringField('Введите название товара ', validators=[DataRequired()])
    supplier_id = SelectField('Выберите поставщика', coerce=int)
    prod_type = StringField('Введите тип товара ', validators=[DataRequired()]) 
    prod_amount = IntegerField('Введите кол-во товара ', validators=[DataRequired()])
    prod_price = IntegerField('Введите цену товара ', validators=[DataRequired()])
    submit = SubmitField('Добавить товар')


        