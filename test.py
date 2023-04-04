from bs4 import BeautifulSoup
import requests

# url = 'https://olivkafood.ru/page/menu/6'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.998 Yowser/2.5 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest'
# }
#
# response = requests.get(url=url, headers=headers)
# # print(response.content)
#
# soup = BeautifulSoup(response.text, 'lxml')

html_doc = 'template_html/main.html'
soup = BeautifulSoup(open(html_doc), 'lxml')


def get_menu_to_list(day_number):
    lunch_dict = dict()
    dinner_dict = dict()
    return_dict = dict()

    menu = soup.find_all('div', class_=f'menu-item mix menu-category-filter c{day_number}', limit=2)

    def add_to_dict(name_dict, items, price):
        item_list = list()
        for item in items[1:]:
            if item.text != '':
                item_list.append(item.text)
        name_dict['food'] = item_list
        name_dict['name'] = items[0].text
        name_dict['price'] = price

    for element in menu:
        price_lunch = element.find('div', class_='item-price').text
        if price_lunch == '450Р.':
            item_lunch = element.find_all('div', class_='item-name')
            add_to_dict(name_dict=lunch_dict, items=item_lunch, price=price_lunch)
        else:
            item_dinner = element.find_all('div', class_='item-name')
            add_to_dict(name_dict=dinner_dict, items=item_dinner, price=price_lunch)

    return_dict['lunch'] = lunch_dict
    return_dict['dinner'] = dinner_dict
    return return_dict


print(get_menu_to_list(2))
