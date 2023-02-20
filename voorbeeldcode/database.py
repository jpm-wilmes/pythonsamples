# programma dat met een database communiceert. De database is dezelfde als die voor C# tests
# maakt verbinding met mysql test/test/test op localhost
# doet query op de database (uitlezen tabel)
# print inhoud in de terminal
#
# Jeroen Wilmes 2023

# benodigde driver (installeer via PIP in cmd)
import mysql.connector
# verbind met de database
mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="test"
)
# maak object om queries uit te voeren 
mycursor = mydb.cursor()
# haal content database op in object mycursor
mycursor.execute("SELECT * FROM test")
# laat alle inhoud van de inhoud van mycursor zien
for x in mycursor:
    print(x);