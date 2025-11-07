'''
Récupérer le contenu d’une page web avec requests
L’analyser avec BeautifulSoup
Et enfin afficher le résultat dans ton navigateur (pour visualiser le HTML extrait)
'''

import requests
from bs4 import BeautifulSoup
import webbrowser

url = "https://www.google.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    html_content = soup.prettify()
    with open("resultat_scraping.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open("resultat_scraping.html")
else:
    print(f"Erreur {response.status_code} lors de la requête")
