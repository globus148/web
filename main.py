from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль автронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
