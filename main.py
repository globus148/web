from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/load_photo')
def form_sample():
    return render_template("index.html   ")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
