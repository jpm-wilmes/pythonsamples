# Programma dat laat zien hoe je een functie kunt "tekenen"
# De functie staat in bereken_y()
# Je hebt voor de schermplot een module mathplotlib nodig. Hier vind je die: https://pypi.org/project/matplotlib/
#
# Jeroen Wilmes 2023
#
# deze module alleen voor een plot, niet voor de robot
import matplotlib.pyplot as plt # module om een grafiek te tekenen
# deze module is nodig om te kunnen rekenen
import math # voor sqrt() functie

# definieer radius en offsets en arrays voor de opslag van de functiewaardes voor de grafiek
r = 50 
x_range = 0 # deze waarde moet midden tussen de minimale en maximale positie van de arm komen
x_o = 0 +r # waardes schuiven een stukje (r) op om altijd positieve x en y waardes te hebben
y_o = 0 +r
ar_x = [] # voor de schermplot moeten de resultaten in een array komen. Dit is de declaratie
ar_y = []

# maak functie voor berekenen y waarde
def bereken_y(x, r):
    y = int(math.sqrt(r*r - x*x))
    return y

# functie uitvoeren voor een range x waardes
# omdat het een plot van een cirkel moet worden is eerst de bovenste helft van de cirkel gedaan
# en daarna de onderste helft
# Q1 en Q2 (positieve waardes van de cirkelbderekening)
x = 0-r
while x <= r:
  y = int(bereken_y(x,r))
  # voeg waardes toe aan x en y arrays met offset om altijd positieve waardes te hebben
  ar_x.append(x+x_o+r+x_range) # +r om altijd positieve waardes
  ar_y.append(y+y_o+r)   # +r om altijd positieve waardes
  x += 1 # de volgende positie op de x-as

#Q4 en Q3 (negatieve waardes van de cirkelberekening)
x = r
while x >= (0-r):
  y = 0-int(bereken_y(x,r))
  # voeg waardes toe aan x en y arrays met offset om altijd positieve waardes te hebben
  ar_x.append(x+x_o+r+x_range)
  ar_y.append(y+y_o+r)
  x -= 1

# genereer de grafiek
plt.plot(ar_x, ar_y)
# beschrijving van de grafiek
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('De ronde curve')
# grafiek laten zien
plt.show()

