def parse(query: str) -> dict:
    result = {}

    # check if splitter '?' is missing
    if not '?' in query:
        return result

    # check if parameters exist?
    # url_parts1 = query.split('?')
    url_parts = []
    url_param_delimiter = query.index('?')
    url_parts.extend([query[:url_param_delimiter], query[url_param_delimiter + 1:]])

    if not url_parts[1]:
        return result
    # check if params exist so split them to list by splitter '&'
    else:
        params = url_parts[1].split('&')
        for i in params:
            # check if returned empty parameter
            if not i:
                continue
            equal_elem_num = i.index('=')
            result.update({i[:equal_elem_num]: i[equal_elem_num + 1:]})

            # x = i.split('=')
            # update the result in the proper output format
            # result.update({x[0]: x[1]})
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    #
    assert parse('http://example.com&?') == {}
    assert parse('http://example.com/?name=Dima?&color=purple') == {'name': 'Dima?', 'color': 'purple'}
    assert parse('http://example.com/?name=Dima??????&color=purple') == {'name': 'Dima??????', 'color': 'purple'}
    assert parse('http://example.com/?name=Dima??????&color==purple') == {'name': 'Dima??????', 'color': '=purple'}
    assert parse('http://example.com/??name=Dima') == {'?name': 'Dima'}
    assert parse('http://example.com/????name=Dima') == {'???name': 'Dima'}
    # assert parse('http://example.com/?=') == {''}


def parse_cookie(query: str) -> dict:
    result = {}
    # print(query.index('=')) #4 posle 4 splituem

    #  check if empty
    if not query:
        return result

    # check '=' not exist
    if not '=' in query:
        return result

    # if not ';' in query:
    #     pass
    # split by key-value blocks
    obj = query.split(';')

    # main logic: output in cookie format
    for i in obj:
        # skip if empty element
        if not i:
            continue
        # get num of element of '=' and split by 2 parts
        equal_elem_num = i.index('=')
        result.update({i[:equal_elem_num]: i[equal_elem_num + 1:]})
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('name=Dima') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;age=28') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age==28;') == {'name': 'Dima=User', 'age': '=28'}
    assert parse_cookie(';name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';name=Dima=User;age=28') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name') == {}
    assert parse_cookie(';') == {}
