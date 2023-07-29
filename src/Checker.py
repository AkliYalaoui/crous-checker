import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any bad response status code
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the website: {e}")
        return None

def check_for_logement(html, target_class):
    soup = BeautifulSoup(html, 'html.parser')
    h2_tag = soup.find_all('h2', class_=target_class)
    
    if len(h2_tag) == 0: 
        return False, "Aucun logement trouvé"
    
    if "Aucun" in h2_tag[0].text :
        return False, "Aucun logement trouvé"

    return True, h2_tag[0].text
