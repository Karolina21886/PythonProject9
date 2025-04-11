import requests
from bs4 import BeautifulSoup

class BooksScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None
        self.rating_dict = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        books = []
        cards = self.soup.select(".product_pod")[:8]
        for card in cards:
            title = card.h3.a["title"]
            price = card.select_one(".price_color").text
            rating_class = card.p["class"][1]
            rating = self.rating_dict.get(rating_class, "Невідомо")

            books.append({
                'Назва': title,
                'Ціна': price,
                'Рейтинг': f"{rating} Зірок"
            })
        return books

    def showInfo(self):
        print(f"{'НАЗВА':<60}{'ЦІНА':<10}{'РЕЙТИНГ'}")
        print("-" * 90)
        for book in self.getInfo():
            print(f"{book['Назва']:<60}{book['Ціна']:<10}{book['Рейтинг']}")

url = 'http://books.toscrape.com'
scraper = BooksScraper(url)
scraper.auditSite()
if scraper.soup:
    print("Перші 8 книг на Books to Scrape:")
    scraper.showInfo()
else:
    print("Жодної інформації не отримано")