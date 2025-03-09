from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class SuppForm(FlaskForm):
    sup_name = StringField('Введите имя поставщика: ', validators=[DataRequired()])
    address = StringField('Введите адрес поставщика: ', validators=[DataRequired()] )
    phone_number = IntegerField('Введите номер телефона поставщика: ', validators=[DataRequired()])
    submit = SubmitField('Создать поставщика')