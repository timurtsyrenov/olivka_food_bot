import textwrap
import requests
from bs4 import BeautifulSoup

from utils.get_time import get_today_str
from utils.log_app import logger

"""
Скрипт, получающий html страницу и парсящий ее в списки обедов по дням недели.
"""


class LunchMenu:
    """
    Описание класса LunchMenu.
    Этот класс содержит метод для вывода меню обеда на день.
    """

    def __init__(self, lunch_name, lunch_price, lunch_items, day):
        """
        Конструктор класса.
        Аргументы:
        lunch_name -- Название обеда.
        lunch_price -- Цена обеда.
        lunch_items -- Список блюд на обед.
        str_day -- День обеда.
        """
        self.lunch_name: str = lunch_name
        self.lunch_price: str = lunch_price
        self.lunch_items: list = lunch_items
        self.str_day: str = get_today_str(day)

    def __str__(self):
        # Два list comprehension один добавляет перенос для слов длиннее 30 символов, другой распаковывает список
        menu = '\n'.join([item for item in [textwrap.fill(pos, 30) for pos in self.lunch_items]])
        # Формируем результирующую строку всего меню
        return (
            f"Меню на {self.str_day} \n\n"
            f"{self.lunch_name} - {self.lunch_price} \n\n"
            f"{menu}"
        )


class WebParser:
    """
    Описание класса WebParser.
    Этот класс содержит метод для парсинга html страницы с обедом.
    """

    def __init__(self, day: int):
        """
        Конструктор класса.
        Аргументы:
        url -- Адрес запроса.
        headers -- Заголовки запроса.
        day -- День обеда.
        """
        self.url: str = "https://olivkafood.ru/page/menu/6"
        self.headers: dict = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.998 Yowser/2.5 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.day: int = day

    def parse(self) -> LunchMenu:
        """
        Метод для парсинга и обработки данных с сайта оливки.
        Возвращает объект класса LunchMenu с меню обеда на день.
        :return class LunchMenu: Фотография с меню
        """

        try:
            # Посылаем запрос на сайт olivkafood.ru для получения html страницы
            response = requests.get(url=self.url, headers=self.headers, timeout=5)
            if response.content is not None:
                # Получаем html страницу
                soup = BeautifulSoup(response.text, "lxml")
                logger.success(f"Запрос к {self.url} | {response.status_code}")
                # Поиск html класса menu-item mix menu-category-filter c{Номер дня}
                menu = soup.find_all("div", class_=f"menu-item mix menu-category-filter c{self.day}", limit=2)
                logger.trace(f"menu = {menu}")
                # Поиск html класса item-name, содержащий названия блюд
                items = menu[1].find_all('div', {'class': 'item-name'})
                # Слова которые необходимо исключить
                black_text = ['(ПРАВЫЙ БЕРЕГ)', '(ЛЕВЫЙ БЕРЕГ)']
                # Формируем список обеда за 300 рублей из всех блюд ['Салат', 'Суп', 'Котлета', 'Морс']
                # Используем два list comprehension 1 убирает лишние слова, 2 обрезает пробелы и убирает 0 элемент
                lunch_items: list = [item.text.strip().replace(black_text[0], '').strip() for item in items if
                                     item.text.strip() and black_text[1] not in item.text.strip()]
                # Формируем строку с ценой обеда "300Р."
                lunch_price: str = menu[1].find('div', {'class': 'item-price'}).text.strip()
                # Формируем строку с названием обеда "Обед до 16:00"
                lunch_name: str = lunch_items[0]
                # Создаем объект класса LunchMenu
                return LunchMenu(lunch_name=lunch_name,
                                 lunch_price=lunch_price,
                                 lunch_items=lunch_items[1:],
                                 day=self.day)
            else:
                logger.exception("Нет данных от сайта Оливки")
                # return 'Нет данных от сайта Оливки' # нужно передать админу? или всем пользователям
        except requests.exceptions.RequestException as e:
            logger.exception(f"HTTP error: {e}")
