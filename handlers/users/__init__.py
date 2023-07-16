# Тут мы импортируем все хендлеры
from .today import dp
from .start_and_menu import dp
from .off_notification import off_notification
from .on_notification import on_notification
from .set_custom_time import set_custom_time

# Список параметров который можно импортировать из папки users
__all__ = ["dp"]
