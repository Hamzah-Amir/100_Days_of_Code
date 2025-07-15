import requests
import json
query = input("What topic of news do you want to read? ")
source = input("Enter news source ID (e.g., bbc-news, cnn, techcrunch): ")
language = input("Enter 2-letter language code (e.g., en, fr, es): ")

url = f"https://newsapi.org/v2/everything?q={query}&sources={source}&language={language}&from=2025-06-15&sortBy=publishedAt&apiKey=430298b198374d37a64a3a86c6447563"

r = requests.get(url)
news = json.loads(r.text)

for i, article in enumerate(news["articles"]):
    if i>= 2 :
        break
    print(f"Titile: {article["title"]}\n")
    print(f"Description: {article["description"]}\n")
    print(f"Content: {article["content"]}")