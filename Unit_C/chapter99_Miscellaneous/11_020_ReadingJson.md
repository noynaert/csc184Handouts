# 11.020 Reading JSON from files and URLs

## Minified vs Prettified

### Minified JSON

```json
{"name":"Rand Al'Thor","age":20}
```

### Prettified JSON

```json
{ 
    "name": "Rand Al'Thor", 
    "age": 20 
}
```

[https://codebeautify.org/jsonminifier](https://codebeautify.org/jsonminifier)

## Reading from a local file

```json
# readFile.py

import json

fileName = "person.json"

# Opening JSON file
f = open(fileName)

# returns JSON object as
# a dictionary
person = json.load(f)

# close the file
f.close()

print(person)
```

## Reading from a URL

```python
# read JSON from a URL

import json
import requests

address = "http://worldtimeapi.org/api/timezone/America/Chicago"

url = requests.get(address)

print(url.text)
data = json.loads(url.text)
print(data)
print(data["abbreviation"])
```

# Some other URLs

* ISS: [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)
* Bitcoin: [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json)
* NBA: [https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json](https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json)
* Time: [http://worldtimeapi.org/api/timezone/America/Chicago](http://worldtimeapi.org/api/timezone/America/Chicago)
