import sqlite3

LOCATION = "olivka_food_bot.sqlite"

# Инициализируем переменную базы данных и создаем ее файл
with sqlite3.connect(LOCATION) as conn:
    cursor = conn.cursor()
    # Создаем таблицу, первичным ключем является chat id
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS notification (
        chat_id INTEGER NOT NULL PRIMARY KEY,
        time TEXT NOT NULL DEFAULT "10:00",
        status INTEGER NOT NULL DEFAULT 1)
        """
    )
    # Сохраняем изменения с помощью функции commit для объекта соединения
    conn.commit()
    # Закрыть соединение с базой данных
    # conn.close()



# Команда удаления таблицы
# cur.execute("""DROP TABLE notification""")


def create_user(chat_id: int):
    """
    Функция добавляет нового пользователя в базу данных при вводе команды start
    :param int chat_id: chat id пользователя
    :return:
    """
    # Формируем данные записи
    data = [(chat_id, 1, "10:00")]
    # Подготавливаем множественный запрос
    sql = "INSERT INTO notification (CHAT_ID, TIME, STATUS) values(?, ?, ?)"
    # Загружаем данные в базу
    cursor.executemany(sql, data)
    # вывод данных
    # with db:
    #     data = db.execute("SELECT * FROM notification")
    #     for row in data:
    #         print(row)


# create_new_user(123123)


def get_user_from_table(chat_id: int):
    """
    Функция проверяет наличие записи в таблице, если запись есть возвращает его настройки
    :param int chat_id: chat id пользователя
    :return: tuple result: кортеж с данными записи о пользователе
    """
    # Подготавливаем запрос
    sql = f"SELECT * FROM notification WHERE chat_id = {chat_id}"
    # Делаем запрос в базу данных
    try:
        result = cursor.execute(sql).fetchone()
        return result
    except:
        return "Записи с таким chat id нет"


# print(get_user_from_table(123123))


def on_notification(chat_id: int):
    """
    Функция для внесения в поле on_off значения 1(on)
    :param int chat_id: chat id пользователя
    :return:
    """
    pass


def off_notification(chat_id: int):
    """
    Функция для внесения в поле on_off значения 0(off)
    :param int chat_id: chat id пользователя
    :return:
    """
    pass


def set_time_notification(chat_id: int, time: str):
    """
    Функция для внесения в поле time пользовательского времени
    :param int chat_id: chat id пользователя
    :param str time: устанавливаемое время в формате HH:MM
    :return:
    """
    pass
