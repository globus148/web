from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/load_photo', methods=['POST', 'GET'])
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
    <style>
      #preview {{
        max-width: 100%;
        height: auto;
        margin-top: 10px;
        margin-bottom: 10px;
        display: none;
      }}
    </style>
  </head>
  <body>
    <div class="container mt-5">
      <div class="text-center mb-4">
        <h1>Загрузка фотографии <br> для участия в миссии</h1>
      </div>
      <form class="login_form d-flex flex-column align-items-center" method="post" enctype="multipart/form-data">
        <div class="mb-3 w-80">
          <label for="photo" class="form-label">Приложите фотографию</label>
          <input type="file" class="form-control" id="photo" name="file" onchange="previewFile()">
          <img id="preview" src="#" alt="Preview Image">
        </div>
        <button type="submit" class="btn btn-primary mt-3">Отправить</button>
      </form>
    </div>
    <script>
      function previewFile() {{
        const preview = document.getElementById('preview');
        const file = document.getElementById('photo').files[0];
        const reader = new FileReader();

        reader.addEventListener("load", function () {{
          preview.src = reader.result;
          preview.style.display = 'block';
        }}, false);

        if (file) {{
          reader.readAsDataURL(file);
        }}
      }}
    </script>
  </body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
