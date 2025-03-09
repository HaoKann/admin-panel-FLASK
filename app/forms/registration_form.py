from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models.user import User

class RegForm(FlaskForm):
    name = StringField('Введите имя: ')
    username = StringField('Введите логин: ', validators=[DataRequired()])
    email = EmailField('Введите email: ', validators=[DataRequired()])
    phone_number = IntegerField('Введите номер телефона: ', validators=[DataRequired()])
    password1 = PasswordField('Введите пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль',validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Зарегестрироваться')

    def validate_username(form, username):
        if len(username.data) < 3:
            raise ValidationError('Имя должно содержать более 3 символов')
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пользователь с таким именем уже существует. Выберите другое имя.')
        
    def vaidate_password1(form, password1):
        if len(password1.data) < 5:
            raise ValidationError('Пароль должен содержать более 5 символов')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пользователь с таким email уже существует. Выберите другой email.')