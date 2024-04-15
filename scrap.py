import requests
from bs4 import BeautifulSoup
import json


def scrape_rozetka():
    url = "https://rozetka.com.ua/mobile-phones/c80003/preset=smartfon;producer=apple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    phones = soup.find_all('div', class_='goods-tile')

    phone_list = []
    for phone in phones:

        name = phone.find('span', class_='goods-tile__title').text
        colors = phone.find('span', class_='goods-tile__colors-content').text
        # ram = phone.find('div', class_='goods-tile__details').find('ul').find_all('li')[0].text
        price = phone.find('span', class_='goods-tile__price-value').text
        # storage = phone.find('div', class_='goods-tile__details').find('ul').find_all('li')[1].text

        phone_dict = {
            'Name': name,
            'Colors': colors,
            # 'RAM': ram,
            'Price': price,
            # 'Storage': storage
        }

        phone_list.append(phone_dict)

    with open('phones.json', 'w', encoding='utf-8') as f:
        json.dump(phone_list, f, ensure_ascii=False, indent=4)


scrape_rozetka()

