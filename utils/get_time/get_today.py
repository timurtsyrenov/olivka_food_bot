import datetime


def get_today() -> int:
    """
    Функция возвращает текущий день недели
    :return int today: День недели
    """
    today = datetime.datetime.today().weekday() + 1
    return today
