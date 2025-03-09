from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class SupportForm(FlaskForm):
    type_of_question = SelectField('Выберите тип вопроса:', choices=[
        ('Проблемы с регистрацией', 'Проблемы с регистрацией'),
        ('Проблема с оплатой', 'Проблема с оплатой'),
        ('Другое','Другое')], validators=[DataRequired()])
    name = StringField('Введите своё имя:')
    email_for_reply = EmailField('Ввёдите адрес электронной почты, на которую придет ответ:')
    question = TextAreaField('Введите вопрос:')
    submit = SubmitField('Отправить обращение')
    
class RespondAppeal(FlaskForm):
    response_field = TextAreaField('Введите ответ на обращение:')
    submit = SubmitField('Отправить ответ на обращение')