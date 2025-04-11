import requests
from bs4 import BeautifulSoup

class RozetkaScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        products = []
        cards = self.soup.find_all('div', class_='goods-tile')[:8]  # Перші 8 смартфонів
        for card in cards:
            name_tag = card.find('span', class_='goods-tile__title')
            price_tag = card.find('span', class_='goods-tile__price-value')

            name = name_tag.text.strip() if name_tag else 'Назва відсутня'
            price = price_tag.text.strip() + ' грн' if price_tag else 'Ціна відсутня'

            products.append({
                'Назва': name,
                'Ціна': price
            })
        return products

    def showInfo(self):
        print(f"{'НАЗВА':<70}{'ЦІНА'}")
        print("-" * 90)
        for item in self.getInfo():
            print(f"{item['Назва']:<70}{item['Ціна']}")

url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
scraper = RozetkaScraper(url)
scraper.auditSite()
if scraper.soup:
    print("Популярні смартфони на Rozetka:")
    scraper.showInfo()
else:
    print("Жодної інформації не отримано")