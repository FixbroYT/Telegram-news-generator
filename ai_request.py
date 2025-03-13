import requests
from parser import get_text_for_ai
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://api.deepinfra.com/v1/inference/meta-llama/Llama-2-70b-chat-hf"
HEADERS = {"Authorization": "Bearer " + os.getenv("API_KEY")}


def generate_post(prompt: str, max_tokens: int = 200):
    data = {"input": prompt, "max_tokens": max_tokens}

    response = requests.post(API_URL, headers=HEADERS, json=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("results", [{}])[0].get("generated_text", "Ошибка: нет текста в ответе")
    else:
        return f"Ошибка {response.status_code}: {response.text}"


def get_output():
    data = get_text_for_ai()
    news_text = data[0]
    article_url = data[1]

    text = f"""
    Напиши LinkedIn-пост (на английском) на основе статьи ниже.  
    ✅ **Длина**: не более 5 предложений.  
    ✅ **Структура**: 1 цепляющая фраза + 3-4 предложения + призыв к действию.  
    ✅ **Добавь смайлики**, но не больше 5.  
    ✅ **Стиль**: профессиональный, но лёгкий и энергичный.  
    ✅ **Дополнительно**: добавь ссылку на статью {article_url}.  

    Ответь **только одним вариантом поста**, без пояснений, без повторов и без предложений исправить что-то.

    Вот статья: {news_text}
    """

    output = generate_post(text)

    return output

def get_post_text():
    text = get_output()
    return text
