# from flask import Flask, url_for, render_template
# 
# app = Flask(__name__)
# 
# 
# @app.route('/')
# @app.route('/index')
# def index():
#     return "Привет, Яндекс!"
# 
# 
# @app.route('/load_photo')
# def form_sample():
#     return render_template("index.html   ")
# 
# 
# if __name__ == '__main__':
#     app.run(port=8080, host='127.0.0.1')
from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Создаем папку для загрузок, если ее нет
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return "Привет, Яндекс!"


@app.route('/load_photo', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Проверяем, есть ли файл в запросе
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # Если пользователь не выбрал файл
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Сохраняем файл
            filename = 'uploaded_photo.' + file.filename.rsplit('.', 1)[1].lower()
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Перенаправляем на страницу с результатом
            return redirect(url_for('upload_file', success=True))

    # Проверяем, есть ли сохраненное изображение
    uploaded_image = None
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.startswith('uploaded_photo.'):
            uploaded_image = url_for('static', filename=f'uploads/{filename}')
            break

    return render_template('upload_form.html',
                           uploaded_image=uploaded_image,
                           success=request.args.get('success'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

