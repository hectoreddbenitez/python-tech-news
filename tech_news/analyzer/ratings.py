from collections import Counter
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
    list = []
    response = database.find_news()

    for new in response:
        list.append(new["category"])
    ordered_list = sorted(list)
    categories_count = Counter(ordered_list).most_common()
    top_5 = []
    for item in categories_count:
        top_5.append(item[0])
    return top_5
