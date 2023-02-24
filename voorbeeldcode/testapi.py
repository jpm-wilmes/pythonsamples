# programma dat speelt met een api
# benodigde module
# testkey van overheid.io (maandelijks verversen)
# getvariabele key: ?ovio-api-key=0b8e03b7e03ba082be304878df9c78cfaf13ad91d06fdf2decffd780d77f0c9e

import requests
import json

KENTEKEN    = '/P280KK'
URL         = 'https://api.overheid.io/voertuiggegevens'
PARAMS      = {'ovio-api-key': '0b8e03b7e03ba082be304878df9c78cfaf13ad91d06fdf2decffd780d77f0c9e', \
               }
# haal de gegevens op via de api
response = requests.get(url = URL + KENTEKEN , params = PARAMS)
# laat inhoud zien in json format
data = response.json()
print(data['handelsbenaming'])
print(data['eerste_kleur'])

