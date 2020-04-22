def parse(query: str) -> dict:
    result = {}

    # check if splitter '?' is missing
    if not '?' in query:
        return result

    # check if parameters exist?
    url_parts = query.split('?')
    if not url_parts[1]:
        return result
    # check if params exist so split them to list by splitter '&'
    else:
        params = url_parts[1].split('&')
        for i in params:
            # check if returned empty parameter
            if not i:
                continue
            x = i.split('=')
            #update the result in the proper output format
            result.update({x[0]: x[1]})

    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


