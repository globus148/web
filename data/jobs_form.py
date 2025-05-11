from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.fields import DateTimeField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class JobsForm(FlaskForm):
    team_leader = IntegerField('ID руководителя', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объем работы (часы)', validators=[DataRequired()])
    collaborators = StringField('Участники (через запятую)', validators=[DataRequired()])
    start_date = StringField('Дата начала', validators=[DataRequired()])  # Изменено на StringField
    end_date = StringField('Дата окончания')  # Изменено на StringField
    is_finished = BooleanField('Работа завершена')
    submit = SubmitField('Сохранить')