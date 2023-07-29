import os
from src.Checker import scrape_website, check_for_logement
from src.Notification import send_notification
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":

    bounds = os.getenv("bounds")
    url =  os.getenv("url") + bounds

    target_class = "SearchResults-desktop fr-h4 svelte-11sc5my"
    target_email = "ia_abedmeraim@esi.dz"

    html_content = scrape_website(url)
    if html_content:
        found, msg = check_for_logement(html_content, target_class)
        if not found:
            print("Aucun logement trouvé")
        else:
            print(msg)
            send_notification(target_email, msg, url)
