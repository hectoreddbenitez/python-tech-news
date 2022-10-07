import tech_news

database = tech_news.database


def top_5_news():
    list = []
    response = database.find_news()
    ordered_response = sorted(
        response, key=lambda item: item["comments_count"], reverse=True
    )
    for item in ordered_response[:5]:
        list.append((item["title"], item["url"]))
    return list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
