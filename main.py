from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"

@app.route('/list_prof/<list>')
def show_professions(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель',
                  'врач', 'климатолог', 'астрогеолог',
                  'метеоролог', 'специалист по радиационной защите']
    return render_template("index.html", list_type=list, professions=professions)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
