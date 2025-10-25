# Тут мы импортируем все хендлеры
from .off_notification import off_notification
from .on_notification import on_notification
from .set_custom_time import set_custom_time
from .start_and_menu import router as start_router
from .today import router as today_router

# Список параметров который можно импортировать из папки users
routers = [start_router, today_router]
