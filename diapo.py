from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

browser = webdriver.Chrome()

# Liste des URLs
urls = [
    'https://trello.com/b/HvvFt6zB/global-2023-2024',
    'https://trello.com/b/7Wwo52in/communication-2023-2024',
    'https://trello.com/b/UzTPByBA/event-2023-2024',
    'https://trello.com/b/420eTmFG/sponsoring-2023-2024',
    'https://trello.com/b/rDH09a0K/openlab-2023-2024',
    'https://tinyurl.com/55bfradx',
    'https://tinyurl.com/axtnw8a',
    'https://tinyurl.com/mvf6c6an',
]

# Charger la page de connexion pour récupérer les cookies
browser.get('https://trello.com/login')
time.sleep(5)  # Attendre un peu pour que la page se charge

# Récupérer les cookies
cookies = browser.get_cookies()

# Fermer le navigateur, vous pouvez le réutiliser avec les cookies récupérés
browser.quit()

# Nouveau navigateur
browser = webdriver.Chrome()

# Charger les cookies
browser.get('https://trello.com')  # Chargez n'importe quelle page pour initialiser les cookies
for cookie in cookies:
    browser.add_cookie(cookie)

try:
    while True:
        for url in urls:
            # Charger l'URL
            browser.get(url)

            # Attendre un peu pour que la page se charge
            time.sleep(10)

except KeyboardInterrupt:
    print("Arrêt du diaporama.")
    browser.quit()
