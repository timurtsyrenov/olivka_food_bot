# Тут мы импортируем все хендлеры
from .get_menu import dp
from .button_in_get_menu import dp
from .start import dp
import loader


__all__ = ["dp", "loader"]  # Список парамметров который можно импортировать из папки users
