import tech_news

database = tech_news.database


def search_by_title(title):
    lista = []
    response = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    for item in response:
        lista.append((item["title"], item["url"])) 
    return lista


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
