import tech_news
from datetime import datetime

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
    lista = []
    try:
        # referencia strptime
        # https://parzibyte.me/blog/2020/04/23/validar-fecha-python/
        # referencia strftime:
        # https://www.programiz.com/python-programming/datetime/strftime
        dateOk = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        response = database.search_news(
            {"timestamp": {"$regex": dateOk, "$options": "i"}}
        )
        for item in response:
            lista.append((item["title"], item["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    return lista


# Requisito 8
def search_by_tag(tag):
    lista = []
    response = database.search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    )
    for item in response:
        lista.append((item["title"], item["url"]))
    return lista


# Requisito 9
def search_by_category(category):
    lista = []
    response = database.search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    for item in response:
        lista.append((item["title"], item["url"]))
    return lista
