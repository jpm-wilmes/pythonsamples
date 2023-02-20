# rudimentaire website gebouwd met Python en Flask framework
# demonstreert een webserver (poort 5000 is de default )
#
# Jeroen Wilmes 2023
# 
from flask import Flask

app = Flask(__name__) # name nodig voor instantiering app. De waarde is __main__

# maak de homepage
@app.route('/')
def home():
    return 'Welkom!'

# maak de /about pagina
@app.route('/about')
def about():
    return 'Dit is de "<B>Over ons</B>" pagina'

if __name__ == '__main__': # start de server. HTML returncodes zijn in de terminal te zien
    app.run(port=5000) # de parameter kan worden weggelaten. 5000 is default
    
# starten met
#    http://localhost:5000/
# of http://localhost:5000/about