# programma dat speelt met een api
# benodigde module
# testkey van overheid.io (maandelijks verversen)
# getvariabele key: ?ovio-api-key=0b8e03b7e03ba082be304878df9c78cfaf13ad91d06fdf2decffd780d77f0c9e

import requests

URL         = 'https://api.overheid.io/voertuiggegevens/'
PARAMS      = {'ovio-api-key': '0b8e03b7e03ba082be304878df9c78cfaf13ad91d06fdf2decffd780d77f0c9e', \
               }
kenteken = input("Geef kenteken")
kenteken = kenteken.upper()

# haal de gegevens op via de api
response = requests.get(url = URL + kenteken , params = PARAMS)
data = response.json()
# laat inhoud zien in json format als kenteken bestaat
print("**********************************")
if response.text.find("error") > 0 :
    print("* Kenteken   " + kenteken + " niet gevonden")
else:
    print("* KENTEKEN   " + kenteken)
    print("* Merk       " + data['handelsbenaming'])
    print("* Kleur      " + data['eerste_kleur'])
    print("* APK        " + data['vervaldatum_apk'])
print("**********************************")
