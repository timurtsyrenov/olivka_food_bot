import datetime


def get_today() -> int:
    """
    Функция возвращает текущую дату
    :return int today: текущая дата в виде числа
    """
    today = datetime.datetime.today().weekday() + 1
    return today
