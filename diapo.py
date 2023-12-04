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
    'https://etesiea-my.sharepoint.com/personal/air-esiea_et_esiea_fr/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fair-esiea_et_esiea_fr%2FDocuments%2FAir%20ESIEA%2F01_Administratif%2F2023-2024%2FRèglements%2FReglementIntérieur_V5%2Epdf&parent=%2Fpersonal%2Fair-esiea_et_esiea_fr%2FDocuments%2FAir%20ESIEA%2F01_Administratif%2F2023-2024%2FRèglements',
    
]

try:
    while True:
        for url in urls:
            browser.get(url)
            time.sleep(60)

except KeyboardInterrupt:
    print("Arret du diaporama.")
    browser.quit()
