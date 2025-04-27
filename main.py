from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route("/promotion_image")
def promotion_image():
    return f'''<head> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Жди нас, Марс!</title>
    <style>
        .bg-transparent-opacity {{
            opacity: 0.8;
        }}
    </style>
    </head>
    <body>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <h1>Жди нас, Марс!</h1>
        <img src="/static/img/riana.jpeg">
        <div class="text-bg-primary p-3 bg-transparent-opacity ">Человечество вырастет из детства.</div>
        <div class="text-bg-secondary p-3 bg-transparent-opacity ">Человечеству мала одна планета</div>
        <div class="text-bg-success p-3 bg-transparent-opacity ">Мы сделаем обитаемыми безжизненные пока планеты.</div>
        <div class="text-bg-danger p-3 bg-transparent-opacity">И начнем с Марса!</div>
        <div class="text-bg-warning p-3 bg-transparent-opacity">Присоединяйся!</div>
    </body>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
