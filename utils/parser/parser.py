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


def get_menu_to_list(day_number):
    menu_list = []
    soup = request_page(url, headers)  # получаем html страницу
    logging.debug(soup)
    menu = soup.find_all('div', class_=f'menu-item mix menu-category-filter c{day_number}')
    logging.debug(menu)
    item_list = menu[1].find_all_next('b')
    for n in range(len(item_list)):
        if item_list[n].text == 'Обед до 16.00':
            for i in range(1, 6):
                if item_list[n + i].text.strip() == 'Морс':
                    menu_list.append(item_list[n + i].text.strip())
                    break
                else:
                    menu_list.append(item_list[n + i].text.strip())
            break
        else:
            continue
    return menu_list


# request_page(url, headers)
# monday_menu = get_menu_to_list(1)
# tuesday_menu = get_menu_to_list(2)
# wednesday_menu = get_menu_to_list(3)
# thursday_menu = get_menu_to_list(4)
# friday_menu = get_menu_to_list(5)

# print(monday_menu)
# print(tuesday_menu)
# print(wednesday_menu)
# print(thursday_menu)
# print(friday_menu)
