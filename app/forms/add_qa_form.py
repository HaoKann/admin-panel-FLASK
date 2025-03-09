from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddQA(FlaskForm):
    new_question = StringField('Введите вопрос:', validators=[DataRequired()])
    new_answer = StringField('Введите ответ:', validators=[DataRequired()])
    submit = SubmitField('Отправить данные')