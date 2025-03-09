from flask_wtf import FlaskForm 
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class ChangePassword(FlaskForm):
    old_password = PasswordField('Введите старый пароль: ', validators=[DataRequired()])
    new_password1 = PasswordField('Введите новый пароль: ', validators=[DataRequired()])
    new_password2 = PasswordField('Подтвердите новый пароль: ', validators=[DataRequired(), EqualTo('new_password1', message='Пароли должны совпадать')])
    submit_password = SubmitField('Подтвердить изменение пароля')