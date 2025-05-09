from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    global_init("db/blogs.db")
    app.run(port=8080, host="127.0.0.1")
