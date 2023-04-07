# Тут мы импортируем все хендлеры
from .get_menu import dp
from .today_and_tomorrow import dp
from .start import dp
import loader


__all__ = ["dp", "loader"]  # Список параметров который можно импортировать из папки users
