from flask_wtf import FlaskForm 
from wtforms import SelectField, SubmitField

class ChangeTheme(FlaskForm):
    chosen_theme = SelectField('Выберите тему', choices=[
        ('light', 'Светлая'),
        ('dark', 'Темная')
    ])
    submit= SubmitField('Применить тему')