#
# programma dat inlogt bij een website
#
# haal de driver binnen
import http.client
# definieer de url waar een request naartoe gaat met de juiste poort
conn = http.client.HTTPSConnection("www.gulpdalvakantiewoningen.nl")
conn.request("GET","/")
# de response komt in res (html)
res = conn.getresponse()
# druk af in blokken van 20
while chunk := res.read(20):
    print(repr(chunk))