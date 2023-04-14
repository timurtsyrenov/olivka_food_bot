import datetime
from utils.log_app import logger


def get_today_int() -> int:
    """
    Функция возвращает текущий день недели в виде числа
    :return int today: День недели
    """
    today = datetime.datetime.today().weekday() + 1
    logger.debug(f"today: {today}")
    return today


def get_today_str(weekday_number: int) -> str:
    """
    Функция возвращает текущий день недели в виде строки
    :param int weekday_number: День недели в виде числа
    :return str today: День недели в виде строки
    """
    # Список дней недели, при этом индекс 0 указан как "Дни недели"
    weekdays = ["Дни недели", "Понедельник", "Вторник", "Среду", "Четверг", "Пятницу"]
    # Получение названия дня недели по индексу
    weekday_name = weekdays[weekday_number]
    return weekday_name
