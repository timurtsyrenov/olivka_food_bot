# Тут мы импортируем все хендлеры
from .today import dp
from .start import dp
import loader


__all__ = ["dp", "loader"]  # Список параметров который можно импортировать из папки users
