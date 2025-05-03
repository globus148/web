from flask import Flask, url_for, render_template, request, redirect
import json
import random

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет яндекс"


@app.route('/member')
def member():
    with open("C:/Users/utu/PycharmProjects/pythonProject4/templates/crew_data.json" , "r", encoding="utf-8") as f:
        crew = json.load(f)["crew"]
        random_member = random.choice(crew)
        random_member["speciality"] = ", ".join(sorted(random_member["specialties"]))
        return render_template("index.html", member=random_member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
