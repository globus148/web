from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div class="container">
                            <div align="center">
                            <h1>Анкета претендента <br> на участие в миссии</h1>
                            </div>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    </div>
                                    <div class="form-group">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </div>
                                    <div class="form-group">
                                        <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Дошкольное</option>
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label>Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Research_Engineer" value="Инженер-исследователь">
                                          <label class="form-check-label" for="Research_Engineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Build_Engineer" value="Инженер-строитель">
                                          <label class="form-check-label" for="Build_Engineer">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="Пилот">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="doctor" value="Врач">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="Meteorologist" value="Метеоролог">
                                          <label class="form-check-label" for="Meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label>Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        # Выводим все данные формы в консоль
        print("=== Данные формы ===")
        print(f"Фамилия: {request.form.get('surname')}")
        print(f"Имя: {request.form.get('name')}")
        print(f"Email: {request.form.get('email')}")
        print(f"Образование: {request.form.get('education')}")

        # Обработка множественного выбора профессий
        professions = request.form.getlist('profession')
        print("Профессии:", ", ".join(professions) if professions else "Не указано")

        print(f"Пол: {request.form.get('sex')}")
        print(f"Причина участия: {request.form.get('about')}")
        print(f"Готов остаться на Марсе: {'Да' if request.form.get('accept') else 'Нет'}")

        # Информация о загруженном файле
        if 'file' in request.files:
            file = request.files['file']
            if file.filename:
                print(f"Загружен файл: {file.filename}")
            else:
                print("Файл не загружен")

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')