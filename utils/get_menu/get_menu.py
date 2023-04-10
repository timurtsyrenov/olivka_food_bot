from utils import convert_text_to_image
from utils.parser import get_menu_to_dict


def get_menu(number_today: int) -> bytes:
    """
    Функция возвращает меню блюд на запрошенный день
    :param int number_today: текущая дата в виде числа
    :return str text_message: текущий блюд для отправки пользователю
    """
    menu = get_menu_to_dict(number_today)
    menu_lunch = "\n".join(str(item) for item in menu.get("lunch").get("food"))  # Формируем строку за 450 рублей
    # из всех блюд для отправки пользователю
    menu_dinner = "\n".join(str(item) for item in menu.get("dinner").get("food"))  # Формируем строку за 300 рублей
    # из всех блюд для отправки пользователю
    menu_to_convert = (
        f"Меню на {number_today}: \n"
        f'{menu.get("lunch").get("name")} - {menu.get("lunch").get("price")}\n'
        f"{menu_lunch}\n\n"
        f'{menu.get("dinner").get("name")} - {menu.get("dinner").get("price")}\n'
        f"{menu_dinner}"
    )
    # Преобразовываем строку с меню в изображение в виде потока байтов
    photo_bytes = convert_text_to_image(menu_to_convert)
    return photo_bytes
