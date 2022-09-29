import requests
from time import sleep


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    response = requests.get(url, headers=headers, timeout=3)
    sleep(1)

    try:
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
