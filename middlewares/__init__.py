from .throttling import ThrottlingMiddleware


def setup(dispatcher):
    # Подключаем middleware к сообщениям
    dispatcher.message.middleware(ThrottlingMiddleware())
    # Подключаем middleware к callback_query
    dispatcher.callback_query.middleware(ThrottlingMiddleware())
