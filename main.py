from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/table/<pol>/<int:age>')
def table(pol, age):
    if pol == "male":
        wall_color = "blue"
    elif pol == "female":
        wall_color = "orange"
    else:
        return
    saturate = "100"
    if age < 21:
        img = "child.png"
        saturate = "50"
    else:
        img = "adult.png"
    return render_template("login.html", wall_color=wall_color, image=img, saturate=saturate)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
