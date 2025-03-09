from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

class BillsForm(FlaskForm):
    orderer = StringField('Введите имя владельца счета: ', validators=[DataRequired()])
    bill_number = IntegerField('Введите номер счета: ', validators=[DataRequired()])
    sum_of_bill = IntegerField('Введите сумму счета: ', validators=[DataRequired()])
    date_of_bill = DateField('Введите дату создания счета: ', validators=[DataRequired()])
    submit = SubmitField('Добавить счет')