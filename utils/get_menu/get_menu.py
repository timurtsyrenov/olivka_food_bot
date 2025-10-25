from utils import convert_text_to_image
from utils.log_app import logger
from utils.parser import WebParser
from aiogram.types import BufferedInputFile

def get_menu(number_today: int) -> BufferedInputFile:
    """
    Функция возвращает меню блюд на запрошенный день
    :param int number_today: Текущая дата в виде числа
    :return bytes photo_bytes: Фотография с меню
    """
    # Создаем объект класса WebParser для обращения к сайту olivkafood.ru
    parser = WebParser(number_today)
    # Вызываем метод парсинга страницы для получения меню за день
    menu = parser.parse()
    logger.trace(f"menu_to_convert: {menu.__str__()}")
    # Преобразовываем строку с меню в изображение в виде потока байтов
    photo_bytes = convert_text_to_image(menu.__str__())
    photo_file = BufferedInputFile(photo_bytes, filename="text_image.webp")
    return photo_file
