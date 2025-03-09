from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, IntegerField, FileField, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from flask_login import current_user
from app.models.user import User

class ChangeProfile(FlaskForm):
    name = StringField('Введите своё имя: ')
    username = StringField('Введите имя пользователя: ', validators=[DataRequired()])
    email = EmailField('Введите почту: ',  validators=[DataRequired()])
    phone_number = IntegerField('Введите номер телефона: ')
    photo = FileField('Добавить фото профиля: ', validators=[FileAllowed(['jpg','png','gif'], 'Можно загружать только картинки!' )])
    submit = SubmitField('Изменить данные')

    def validate_username(form, username):
        if len(username.data) < 3:
            raise ValidationError('Имя должно содержать более 3 символов')
        user = User.query.filter_by(username=username.data).first()
        if user is not None and user.id != current_user.id:
            raise ValidationError('Пользователь с таким именем уже существует. Выберите другое имя.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None and user.id != current_user.id:
            raise ValidationError('Пользователь с таким email уже существует. Выберите другой email.')