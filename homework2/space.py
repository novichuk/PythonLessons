import json
import requests

def num_of_astronauts() -> str:
    r = requests.get('http://api.open-notify.org/astros.json')
    result = json.loads(r.text)
    result = str(result['number'])
    return result