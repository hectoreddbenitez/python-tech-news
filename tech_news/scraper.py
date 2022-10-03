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


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    # tirar duvida na mentoria!!
    # url_next_page = selector.css("next page-numbers ::attr(href)").get()
    url_next_page = selector.css(".next ::attr(href)").get()
    if url_next_page is None:
        return None
    return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css("span.author a::text").get().strip()
    coments = len(selector.css(".comment-list li").getall())
    if coments is None:
        coments = 0
    sumary = "".join(
        selector.css(".entry-content > p:first-of-type ::text").getall()
    ).strip()
    tags = selector.css("a[rel=tag]::text").getall()
    category = selector.css(".label ::text").get()

    # referencia(.strip()):
    # https://www.delftstack.com/pt/howto/python/how-to-remove-whitespace-in-a-string/
    # referencia(first-of-type):
    # https://developer.mozilla.org/pt-BR/docs/Web/CSS/:first-of-type
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": coments,
        "summary": sumary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
