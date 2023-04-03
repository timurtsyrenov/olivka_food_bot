import requests
from bs4 import BeautifulSoup

'''
Скрипт, получающий html страницу и парсящий ее в списки обедов по дням недели.
'''

url = 'https://olivkafood.ru/page/menu/6'
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.998 Yowser/2.5 Safari/537.36',
    "X-Requested-With": 'XMLHttpRequest'
}
r = requests.get(url, headers=headers, timeout=30)  # посылаем запрос
soup = BeautifulSoup(r.text, 'lxml')


def get_menu_to_list(day_number):
    menu_list = []
    menu = soup.find_all('div', class_=f'menu-item mix menu-category-filter c{day_number}')
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
