# read JSON from a URL

import json
import requests

address = "http://worldtimeapi.org/api/timezone/America/Chicago"

url = requests.get(address)

print(url.text)
data = json.loads(url.text)
print(data)
print(data["abbreviation"])