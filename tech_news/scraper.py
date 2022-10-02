import requests
from time import sleep
from parsel import Selector


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    sleep(1)

    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    return response.text


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url_news_list = selector.css("h2.entry-title a::attr(href)").getall()
    return url_news_list

# Requisito 3
def scrape_next_page_link(html_content):
    ...


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
