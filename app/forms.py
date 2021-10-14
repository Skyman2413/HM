from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired


class InfoForm(FlaskForm):
    name = StringField("Фамилия", validators=[DataRequired()])
    lname = StringField("Имя", validators=[DataRequired()])
    mname = StringField("Отчество", validators=[DataRequired()])
    executor_name = StringField("Исполнитель", validators=[DataRequired()])
    service_name = StringField("Услуга", validators=[DataRequired()])
    date = DateField('Дата Выставления', format="%d.%m.%Y")
    submit = SubmitField('Отправить')
