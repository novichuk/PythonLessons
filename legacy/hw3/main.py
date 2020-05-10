from db import show_unique_names, count_of_tracks, all_tracks_info, run_query, ordering, filter_and

from flask import Flask, request

app = Flask(__name__)


# MAIN MENU
@app.route("/")
def hello() -> str:
    return """
<!DOCTYPE HTML>
<html>
 <head>
   <meta charset="utf-8">
  <title>HW3</title>
 </head>
 <body>
  <p><a href="/names/">1) Show unique names</a></p>
  <p><a href="/tracks/">2) Amount of tracks</a></p>
  <p><a href="/customers/">3) FILTERS</a></p>
  <p><a href="/tracks-sec/">4) All tracks</a></p>

</body>
</html>
    """


# (2) 1. Вью функция должна выводить количество уникальных имен (FirstName) из таблицы customers.
@app.route("/names/")
def names() -> str:
    result = show_unique_names()
    return result


# (2) 3. Вью функция должна выводить количество записей из таблицы tracks.
@app.route("/tracks/")
def show_count_of_tracks() -> str:
    result = count_of_tracks()
    return result


# (2) 4. Вью функция должна выводить все треки и соответствующую длину трека в секундах из таблицы tracks.
@app.route("/tracks-sec/")
def show_all_tracks_info() -> str:
    result = all_tracks_info()
    result = [f'{track_id + 1}: {dicts_of_tracks[0]} - {round(dicts_of_tracks[1] / 1000, 2)}' for
              track_id, dicts_of_tracks in enumerate(result)]
    result = '<br/>'.join(e for e in result)
    return result


# (4) 2. Реализовать функцию по тестам. Должна быть возможность передавать квери параметр который добавляет фильтрацию по заданным полям и их значениям.
@app.route("/customers/")
def customers():
    query = '''
    SELECT * FROM customers
    '''

    country = request.args.get('country')
    if country:
        param = f"WHERE Country ='{country}'"
        query += param

    filter_args = request.args.get('filter')
    if filter_args:
        param = f" AND {filter_and(filter_args)}"
        query += param

    order = request.args.get('ordering')
    if order:
        param = f" ORDER BY {ordering(order)}"
        query += param



    query += ';'
    print(query)
    return str(run_query(query))


if __name__ == "__main__":
    app.run(port=5051, debug=True)
