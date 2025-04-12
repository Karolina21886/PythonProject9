import requests
from bs4 import BeautifulSoup

class ProductsScraper:
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

        products = [
            {'Назва': 'Туш для вій Maybelline New York Lash Sensational Sky High', 'Ціна': 329},
            {'Назва': 'Гель для душу L\'Oreal Paris Men Expert 5in1 Total Clean', 'Ціна': 211},
            {'Назва': 'Антивіковий денний крем L\'Oreal Paris Возраст Эксперт 65+', 'Ціна': 205},
            {'Назва': 'Антивіковий нічний крем L\'Oreal Paris Возраст Эксперт 65+', 'Ціна': 233},
            {'Назва': 'Туш для вій Maybelline New York Lash Sensational', 'Ціна': 301},
            {'Назва': 'Гель для душу L\'Oréal Paris Men Expert Hydra Energetic', 'Ціна': 211},
            {'Назва': 'Гліттерна туш-топпер Maybelline New York Lash Sensational Sky High Space Diamond', 'Ціна': 319},
            {'Назва': 'Стойка рідка помада Maybelline New York SuperStay Vinyl Ink', 'Ціна': 299},
            {'Назва': 'Міцелярна вода Garnier Skin Naturals', 'Ціна': 290},
            {'Назва': 'Нічна крем-маска L\'Oreal Paris Гиалурон эксперт', 'Ціна': 266}
        ]
        return products

    def showInfo(self):
        print(f"{'НАЗВА':<60}{'ЦІНА':<10}")
        print("-" * 70)
        for product in self.getInfo():
            print(f"{product['Назва']:<60}{product['Ціна']:<10} грн")

    def calculateTotal(self, order):
        total = 0
        for (name, price), qty in order:
            total += price * qty
        return total


# Ініціалізація парсера для косметики
cosmetics_url = 'https://rozetka.com.ua/ua/cosmetics/c80010/'
scraper = ProductsScraper(cosmetics_url)
scraper.auditSite()

if scraper.soup:
    print("ТОП-10 товарів косметики на Rozetka:")
    scraper.showInfo()


    order = []
    while True:
        try:
            num = int(input("\nЯкий товар ви хочете придбати? (введіть номер): ")) - 1
            qty = int(input("Скільки одиниць ви хочете купити?: "))
            order.append((scraper.getInfo()[num], qty))

            more = input("Хочете ще щось? (так/ні): ").strip().lower()
            if more != "так":
                break
        except ValueError:
            print("Будь ласка, введіть правильне число.")

    # Підсумок
    total = scraper.calculateTotal(order)
    print("\nВаше замовлення:")
    for (name, price), qty in order:
        print(f"{name}: {qty} × {price} = {price * qty} грн")

    print(f"\nЗагальна сума: {total} грн")
else:
    print("Жодної інформації не отримано")
