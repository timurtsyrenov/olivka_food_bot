import logging

import requests
from bs4 import BeautifulSoup

'''
Скрипт, получающий html страницу и парсящий ее в списки обедов по дням недели.
'''

url = 'https://olivkafood.ru/page/menu/6'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.998 Yowser/2.5 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def request_page(url_site, headers_bot):
    try:
        r = requests.get(url=url_site, headers=headers_bot, timeout=10)  # посылаем запрос
        if r.content is not None:
            soup = BeautifulSoup(r.text, 'lxml')
            logging.debug(soup)
            return soup
        else:
            logging.error('Нет данных от сайта Оливки')
            return 'Нет данных от сайта Оливки'  # нужно передать админу? или всем пользователям
    except requests.exceptions.HTTPError as e:
        logging.error(f'HTTP error: {e}')
    except requests.exceptions.ConnectionError as e:
        logging.error(f'Connect error: {e}')
    except requests.exceptions.Timeout as e:
        logging.error(f'Timeout: {e}')


def get_menu_to_dict(day_number: int) -> dict:
    lunch_dict = dict()
    dinner_dict = dict()
    return_dict = dict()

    soup = request_page(url, headers)  # получаем html страницу
    # logging.debug(soup)

    menu = soup.find_all('div', class_=f'menu-item mix menu-category-filter c{day_number}', limit=2)

    def add_to_dict(name_dict: dict, items: object, price: str) -> None:
        item_list = list()
        for item in items[1:]:
            if item.text != '':
                item_list.append(item.text.strip())
        name_dict['food'] = item_list
        name_dict['name'] = items[0].text
        name_dict['price'] = price

    for element in menu:
        item_price = element.find('div', class_='item-price').text
        if item_price == '450Р.':
            item_lunch = element.find_all('div', class_='item-name')
            add_to_dict(name_dict=lunch_dict, items=item_lunch, price=item_price)
        else:
            item_dinner = element.find_all('div', class_='item-name')
            add_to_dict(name_dict=dinner_dict, items=item_dinner, price=item_price)

    return_dict['lunch'] = lunch_dict
    return_dict['dinner'] = dinner_dict
    return return_dict
