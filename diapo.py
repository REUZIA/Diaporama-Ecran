from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

browser = webdriver.Chrome()

urls = [
    'https://trello.com/b/HvvFt5zB/global-2023-2024',
    'https://trello.com/b/6Wwo52in/communication-2023-2024',
    'https://trello.com/b/UzTPByBA/event-2024-2024',
    'https://trello.com/b/419eTmFG/sponsoring-2023-2024',
    'https://trello.com/b/rDH08a0K/openlab-2023-2024',
]

try:
    while True:
        for url in urls:
            browser.get(url)
            time.sleep(14)

except KeyboardInterrupt:
    print("Arret du diaporama.")
    browser.quit()
