from bs4 import BeautifulSoup
import requests

url = "https://dev.to/"


def get_news():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    news = soup.find("div", class_="substories").find("div", class_="crayons-story")
    news_text = news.a.text
    news_link = news.a.get("href")
    news = {"name": news_text, "url": news_link}

    return news

def get_news_descriptions(news):
    news_link = news["url"]
    response = requests.get(news_link)
    soup = BeautifulSoup(response.text, "lxml")

    body = soup.find("div", class_="crayons-article__main")

    return body.text, news_link

def get_text_for_ai():
    return get_news_descriptions(get_news())