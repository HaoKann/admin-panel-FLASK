from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class EmployeeForm(FlaskForm):
    name = StringField('Введите имя сотрудника: ', validators=[DataRequired()])
    surname = StringField('Введите фамилию сотрудника: ', validators=[DataRequired()])
    date_of_birth = DateField('Введите дату рождения:', validators=[DataRequired()])
    address = StringField('Введите адрес проживания: ', validators=[DataRequired()])
    salary = IntegerField('Введите заработную плату сотрудника: ', validators=[DataRequired()])
    sumbit = SubmitField('Создать сотрудника')

    def validate_salary(form, salary):
        if salary.data < 100000:
            raise ValidationError('Заработная плата должна быть выше 100000')
        