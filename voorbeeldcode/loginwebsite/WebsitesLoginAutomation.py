#
# programma dat inlogt bij een website
#
# haal de driver binnen
import http.client
# definieer de url waar een request naartoe gaat met de juiste poort
conn = http.client.HTTPConnection("https://gulpdalvakantiewoningen.nl", 80)
#conn.request("HEAD","/index.php")
#res = conn.getresponse()
#print(res.status, res.reason)