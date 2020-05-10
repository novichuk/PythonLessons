from flask import Flask, request
from gen_users import generate_users
from req import read_file
from space import num_of_astronauts
from mean import avg_height_weight

app = Flask(__name__)


# MAIN MENU
@app.route("/")
def hello() -> str:
    return """
<!DOCTYPE HTML>
<html>
 <head>
   <meta charset="utf-8">
  <title>Тег А</title>
 </head>
 <body>
  <p><a href="/requirements/">1) Read requirements.txt file</a></p>
  <p><a href="/generate-users/?amount=100">2) Generate Users</a></p>
    <p><a href="/mean/">3) Characteristic of people</a></p>
  <p><a href="/space/">4) Number of astronauts in space</a></p>

</body>
</html>
    """


# 1. Возвращать содержимое файла с пайтон пакетами (requirements.txt)
@app.route("/requirements/")
def hello_world() -> str:
    return read_file('./requirements.txt')


# 2. Вывести 100 случайно сгенерированных юзеров (почта + имя) + параметр который регулирует количество юзеров
@app.route("/generate-users/")
def gen() -> str:
    amount_users = int(request.args['amount'])
    return generate_users(amount_users)


# 3. Средний рост, средний вес (см, кг) (hw.csv) PATH: /mean/

#
# ДЗ:
# 2. все возвращаем в строку, лист тоже - обернуть в строку
# 3. разбить, перевести во флоаты.
#

@app.route("/mean/")
def mean() -> str:
    result = avg_height_weight().split(',')
    result = f'Average Height: {result[0]} \n Average Weight: {result[1]}'
    return result


# 4. Вывести количество космонавтов в настоящий момент
@app.route("/space/")
def space() -> str:
    result = f'Astronauts in space now: {num_of_astronauts()}'
    return result


if __name__ == "__main__":
    app.run(port=5050, debug=True)
