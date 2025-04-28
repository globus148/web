from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route("/answer")
@app.route('/auto_answer')
def answer():
    book = {
        'title': 'Анкета претендента',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'Высшее',
        'profession': 'Инженер-исследователь',
        'sex': 'male',
        'motivation': 'Хочу стать частью великой миссии!',
        'ready': 'Да'
    }

    return render_template("auto_answer.html", **book)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
