import requests
from bs4 import BeautifulSoup, ResultSet
from utils.log_app import logger

"""
Скрипт, получающий html страницу и парсящий ее в списки обедов по дням недели.
"""

url = "https://olivkafood.ru/page/menu/6"  # Путь к странице сайта Оливки
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.998 Yowser/2.5 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}  # Заголовки запроса


def request_page(url_site: str, headers_bot: dict[str, str]) -> BeautifulSoup:
    """
    Получение страницы сайта, полученная через библиотеку парсинга lxml
    :param str url_site: Адрес сайта
    :param dict[str, str] headers_bot: Заголовки запроса
    :return BeautifulSoup soup: Страница сайта
    """
    try:
        # Посылаем запрос на сайт olivkafood.ru для получения html страницы
        r = requests.get(url=url_site, headers=headers_bot, timeout=10)
        if r.content is not None:
            soup = BeautifulSoup(r.text, "lxml")
            logger.success(f"Запрос к {url} | {r.status_code}")
            return soup
        else:
            logger.exception("Нет данных от сайта Оливки")
            # return 'Нет данных от сайта Оливки' # нужно передать админу? или всем пользователям
    except requests.exceptions.HTTPError as e:
        logger.exception(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
        logger.exception(f"Connect error: {e}")
    except requests.exceptions.Timeout as e:
        logger.exception(f"Timeout: {e}")


def get_menu_to_dict(day_number: int) -> dict:
    """
    Получение состава обеда за запрашиваемый день недели
    :param int day_number: Номер запрашиваемого дня недели
    :return dict return_dict: Словарь с данными обеда за запрошенный день недели
    """
    lunch_dict = dict()
    dinner_dict = dict()
    return_dict = dict()

    # Получаем html страницу
    soup = request_page(url, headers)
    # Ищем тег 'div' классом 'menu-item mix menu-category-filter c{номер дня}'
    # в запрошенной странице с указанием дня недели
    menu = soup.find_all(
        "div", class_=f"menu-item mix menu-category-filter c{day_number}", limit=2
    )
    logger.trace(f"menu = {menu}")

    def add_to_dict(name_dict: dict, items: ResultSet, price: str) -> None:
        """
        Добавление данных по обедам в словарь lunch_dict или dinner_dict
        :param dict name_dict: Словарь с данными обеда за запрошенный день недели
        :param ResultSet items: Список блюд
        :param str price: Стоимость обеда
        """
        item_list = list()
        # Проходимся по списку, пропуская первый элемент т.к первый идет имя обеда
        for item in items[1:]:
            # Если элемент не пустой
            if item.text != "":
                # Добавляем в список блюдо и обрезаем пробелы
                item_list.append(item.text.strip())
        # Добавляем в словарь key 'food' со значением из списка блюд
        name_dict["food"] = item_list
        # Добавляем в словарь key 'name' со значением имени обеда
        name_dict["name"] = items[0].text
        # Добавляем в словарь key 'price' со значением цены
        name_dict["price"] = price

    # Проходимся по найденным тегам и ищем в них lunch и dinner
    for element in menu:
        # Поиск тега с ценой обеда
        item_price = element.find("div", class_="item-price").text
        # Если цена обеда равна 450Р., вызываем добавляем в словарь lunch_dict
        if item_price == "450Р.":
            # Поиск тега с названием обеда
            item_lunch = element.find_all("div", class_="item-name")
            # Добавляем в словарь lunch_dict
            add_to_dict(name_dict=lunch_dict, items=item_lunch, price=item_price)
        else:
            # Поиск тега с названием обеда
            item_dinner = element.find_all("div", class_="item-name")
            # Добавляем в словарь dinner_dict
            add_to_dict(name_dict=dinner_dict, items=item_dinner, price=item_price)
    # Добавляем в словарь key 'lunch': словарь lunch_dict
    return_dict["lunch"] = lunch_dict
    # Добавляем в словарь key 'dinner': словарь dinner_dict
    return_dict["dinner"] = dinner_dict
    logger.trace(f"lunch_dict {lunch_dict}")
    logger.trace(f"dinner_dict {dinner_dict}")
    # Возвращаем итоговый словарь с двумя обедами lunch и dinner
    return return_dict
