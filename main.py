from flask import Flask, render_template, redirect, abort, request
from data.db_session import global_init
from data.login_form import LoginForm
from data import db_session
from data.users import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.News_form import NewsForm
from data.news import News
from data.register_form import RegisterForm
from data.jobs_form import JobsForm
from data.jobs import Jobs
from datetime import datetime
from data.departament_form import DepartamentForm
from data.departament import Departament

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private == False))
    else:
        news = db_sess.query(News).filter(News.is_private == False)
    return render_template("index.html", news=news)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        news.user_id = current_user.id
        db_sess.add(news)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html', title='Редактирование новости', form=form)


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id, News.user == current_user).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", title="Регистрация",
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/works')
def works_list():
    db_sess = db_session.create_session()
    works = db_sess.query(Jobs).all()
    return render_template('work_list.html', title='Список работ', works=works)


@app.route('/add_work', methods=['GET', 'POST'])
@login_required
def add_work():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        work = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            start_date=datetime.strptime(form.start_date.data, '%Y-%m-%d %H:%M') if form.start_date.data else None,
            end_date=datetime.strptime(form.end_date.data, '%Y-%m-%d %H:%M') if form.end_date.data else None,
            is_finished=form.is_finished.data
        )
        db_sess.add(work)
        db_sess.commit()
        return redirect('/works')
    return render_template('add_work.html', title='Добавление работы', form=form)


@app.route('/delete_work/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_work(id):
    db_sess = db_session.create_session()
    work = db_sess.query(Jobs).filter(Jobs.id == id).first()

    if work:
        db_sess.delete(work)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/works')


@app.route('/edit_work/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_work(id):
    db_sess = db_session.create_session()
    work = db_sess.query(Jobs).filter(Jobs.id == id).first()

    # Проверка прав доступа
    if not work or (current_user.id != work.team_leader and current_user.id != 1):  # 1 - ID капитана
        abort(403)  # Доступ запрещен

    form = JobsForm()

    if request.method == 'GET':
        if work:
            form.team_leader.data = work.team_leader
            form.job.data = work.job
            form.work_size.data = work.work_size
            form.collaborators.data = work.collaborators
            form.start_date.data = work.start_date.strftime('%Y-%m-%d %H:%M') if work.start_date else None
            form.end_date.data = work.end_date.strftime('%Y-%m-%d %H:%M') if work.end_date else None
            form.is_finished.data = work.is_finished
        else:
            abort(404)

    if form.validate_on_submit():
        if work:
            work.team_leader = form.team_leader.data
            work.job = form.job.data
            work.work_size = form.work_size.data
            work.collaborators = form.collaborators.data
            work.start_date = datetime.strptime(form.start_date.data,
                                                '%Y-%m-%d %H:%M') if form.start_date.data else None
            work.end_date = datetime.strptime(form.end_date.data, '%Y-%m-%d %H:%M') if form.end_date.data else None
            work.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/works')
        else:
            abort(404)

    return render_template('add_work.html',
                           title='Редактирование работы',
                           form=form)


app.route('/delete_work/<int:id>', methods=['GET', 'POST'])


@login_required
def delete_work(id):
    db_sess = db_session.create_session()
    work = db_sess.query(Jobs).filter(Jobs.id == id).first()

    # Проверка прав доступа
    if not work or (current_user.id != work.team_leader and current_user.id != 1):
        abort(403)

    if work:
        db_sess.delete(work)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/works')


@app.route("/departaments")
def departaments_list():
    db_sess = db_session.create_session()
    departaments = db_sess.query(Departament).all()
    return render_template("departament_list.html",
                           title="Список департаментов", departaments=departaments)


@app.route("/add_departament", methods=["GET", "POST"])
@login_required
def add_departament():
    form = DepartamentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departament = Departament(title=form.title.data,
                                  chief=form.chief.data,
                                  members=form.members.data,
                                  email=form.email.data)
        db_sess.add(departament)
        db_sess.commit()
        return redirect("/departaments")
    return render_template("add_departament.html", title="Добавление департамента",
                           form=form)


@app.route('/edit_departament/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departament(id):
    db_sess = db_session.create_session()
    departament = db_sess.query(Departament).filter(Departament.id == id).first()

    # Проверка прав доступа
    if not departament or (current_user.id != departament.chief and current_user.id != 1):
        abort(403)

    form = DepartamentForm()

    if request.method == 'GET':
        if departament:
            form.title.data = departament.title
            form.chief.data = departament.chief
            form.members.data = departament.members
            form.email.data = departament.email
        else:
            abort(404)

    if form.validate_on_submit():
        if departament:
            departament.title = form.title.data
            departament.chief = form.chief.data
            departament.members = form.members.data
            departament.email = form.email.data
            db_sess.commit()
            return redirect('/departaments')
        else:
            abort(404)

    return render_template('add_departament.html',
                           title='Редактирование департамента',
                           form=form)


@app.route('/delete_departament/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_departament(id):
    db_sess = db_session.create_session()
    departament = db_sess.query(Departament).filter(Departament.id == id).first()

    # Проверка прав доступа
    if not departament or (current_user.id != departament.chief and current_user.id != 1):
        abort(403)

    if departament:
        db_sess.delete(departament)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departaments')


if __name__ == '__main__':
    global_init("db/blogs.db")
    app.run(port=8080, host="127.0.0.1")

