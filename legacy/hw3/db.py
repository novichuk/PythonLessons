import sqlite3


def show_unique_names() -> list:
    conn = sqlite3.connect('chinook.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT DISTINCT Firstname FROM customers;
    ''')
    result = cur.fetchall()
    result = [item[0] for item in result]
    result = '\n'.join(str(e) for e in result)
    conn.close()
    return result


def count_of_tracks() -> str:
    conn = sqlite3.connect('chinook.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT COUNT(*) FROM tracks;
    ''')
    result = cur.fetchone()
    result = str(result[0])
    # result = '\n'.join(str(e) for e in result)
    conn.close()

    return result


def all_tracks_info() -> list:
    conn = sqlite3.connect('chinook.db')
    cur = conn.cursor()
    cur.execute('''
        SELECT Name, Milliseconds FROM tracks;
    ''')
    result = cur.fetchall()
    conn.close()
    return result


# ---------------------------------------------------------------------

def run_query(query: str) -> list:
    try:
        conn = sqlite3.connect('chinook.db')
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results
    except Exception:
        return None
    finally:
        conn.close()


def ordering(query_param: str) -> str:
    """
    country,-city
    """
    result = []
    for elem in query_param.split(','):

        if '-' in elem:
            result.append(f'{elem[1:].capitalize()} DESC')
        else:
            result.append(elem.capitalize())

    return ', '.join(result)


def filter_and(query_param: str) -> str:
    """
    query_params = 'country:USA;city:Boston'
    ?filter=country:USA;city:Boston
    """

    result = []
    for elem in query_param.split(';'):
        elem_res = elem.split(':')
        result.append(f"{elem_res[0].capitalize()} = '{elem_res[1]}'")
    return ' AND '.join(result)



if __name__ == '__main__':
    assert ordering('country,-city') == 'Country, City DESC'
    assert ordering('-country,-city') == 'Country DESC, City DESC'
    assert ordering('') == ''

assert filter_and('country:USA;city:Boston') == "Country = 'USA' AND City = 'Boston'"
assert filter_and('country:USA') == "Country = 'USA'"
assert filter_and('city:Boston') == "City = 'Boston'"
