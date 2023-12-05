from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

browser = webdriver.Chrome()

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

try:
    while True:
        for url in urls:
            browser.get(url)
            time.sleep(60)

except KeyboardInterrupt:
    print("Arret du diaporama.")
    browser.quit()
