from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    order_description = StringField('Введите описание заказа: ', validators=[DataRequired()])
    date = DateField('Введите дату размещения заказа: ', validators=[DataRequired()])
    client_id = SelectField('Выберите клиента: ', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Разместить заказ')