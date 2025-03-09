from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, EmailField, SubmitField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
    name = StringField('Введите имя клиента: ', validators=[DataRequired()])
    phone_number = IntegerField('Введите номер телефона клиента: ', validators=[DataRequired()])
    email = EmailField('Введите email клиента: ', validators=[DataRequired()])
    submit = SubmitField('Добавить клиента ', validators=[DataRequired()])