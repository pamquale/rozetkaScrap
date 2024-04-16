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
        price = phone.find('span', class_='goods-tile__price-value').text

        # Split the name into words
        name_parts = name.split()

        # Initialize storage and color
        storage = None
        color = None

        # Iterate over the name parts
        for i in range(len(name_parts)):
            # If this part ends with 'GB', it's the storage size
            if name_parts[i].endswith('GB'):
                storage = name_parts[i]
                # The next two parts are assumed to be the color
                if i + 2 < len(name_parts):
                    color = name_parts[i + 1] + ' ' + name_parts[i + 2]
                break

        phone_dict = {
            'Name': name,
            'Colors': colors,
            'Price': price,
            'Storage': storage,
            'Color': color
        }

        phone_list.append(phone_dict)

    with open('phones.json', 'w', encoding='utf-8') as f:
        json.dump(phone_list, f, ensure_ascii=False, indent=4)


scrape_rozetka()

