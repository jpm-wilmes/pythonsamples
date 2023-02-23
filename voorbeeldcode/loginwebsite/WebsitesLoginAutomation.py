#
# programma dat inlogt bij een website
#
# gebruikt Chromedriver die gestart moet zijn
#
# De namen van de website invulvelden moeten kloppen 
#
from selenium import webdriver
import yaml # zorg voor yaml bestand ondersteuning

# koppel conf aan de gegevens voor de login
conf = yaml.load(open('loginDetails.yml'))
myName = conf['nu_user']['email']
myPassword = conf['nu_user']['password']

# gebruik de reeds draaiende externe Chromedriver (start deze dus eerst)
driver = webdriver.Chrome()

# routine die de website raadpleegt en de juiste elementen eruit haalt
def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_id(submit_buttonId).click()

login("https://practicetestautomation.com/practice-test-login/", "username", myName, "password", myPassword, "submit")
