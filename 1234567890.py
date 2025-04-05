# шаблон
import requests  # запит
from bs4 import BeautifulSoup as bs


class Name:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалось підключити до сайту")

    def getInfo(self):
        pass

    def showInfo(self):
        pass


url = "посилання"
obj = Name(url)
obj. = auditSite()
site = obj.getInfo()
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримав")

import requests  # запит
from bs4 import BeautifulSoup as bs


class Confy:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser__actions-price-current')
        else:
            print("Не вдалось підключити до сайту")
            return

    def getInfo(self):
        laptop = []
        lap = self.soup.find_all('div', class_='products-catalog')
        if not lap:
            print('Помилка в пошуку на сторінці')
            return laptop
        for i in laptop[0:4]:
            name = i.find('a', class_='prdl-item__name ellipsis-2-lines')
            nameErorr = name.text if name else 'Відсутня назва'
            price = i.find('div', class_='products-list-price..actions-price-current')
            priceEror = price.text() if price else 'Відсутня ціна'
            laptop.apeend(
                {
                    'Назва': name,
                    'Цiна': price,
                }

            )

    return laptop

    def showInfo(self):
        print(f"\t{'Назва':<}\t" * 2, f"{'Ціна':<}\t" * 2)
        print('№\t', 'НАЗВА': <]}\t\t
        {i['Ціна']}
        ")
        url = "https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
        obj = Comfy(url)
        obj. = auditSite()
        site = obj.getInfo()
        print()
        if site:
            obj.showInfo()
        else:
            print("Жодної інформації не отримав")

            # шаблон
            #  from bs4 import BeautifulSoup as bs

            # print ("Не вдалося підключитися до сайту")
            # def getInfo(self): 1 usage new *
            #  coins=[]
            #       listCoin=self.soup.find('tbody')
            #     if not listCoin:
            #     print('Помилка в пошуку на сторінці')
            # return coins
            #  def showInfo (self) : 1 usage new *
            #  pass

            # url="https://coinmarketcap.com/" obj=Coin (url)
            # obj.auditSite ()
            # site=obj.getInfo ()
            # print('5 найпопулярніші криптомонети")
            # if site:
            #   obj.showInfo(site)
            # else:
            #       print ("Жодної інформації не отримано")














