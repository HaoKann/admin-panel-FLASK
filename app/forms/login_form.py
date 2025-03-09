from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Введите имя пользователя: ', validators=[DataRequired()])
    password = PasswordField('Введите пароль: ', validators=[DataRequired()])
    remember = BooleanField('Оставаться в системе')
    submit = SubmitField('Авторизироваться')