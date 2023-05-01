import sqlite3

LOCATION = "olivka_food_bot.sqlite"


# Инициализируем переменную базы данных и создаем ее файл
def connect_db(path):
    with sqlite3.connect(path) as conn:
        return conn
        # Закрыть соединение с базой данных
        # conn.close()


# Команда удаления таблицы
# cur.execute("""DROP TABLE notification""")

def create_table(conn):
    # Создаем таблицу, первичным ключем является chat id
    cursor = conn.cursor()
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
    conn.close()


def create_chat_id(chat_id: int, conn):
    """
    Функция добавляет нового пользователя в базу данных при вводе команды start
    :param int chat_id: chat id пользователя
    :return:
    """
    cursor = conn.cursor()
    if get_chat_id(chat_id, cursor) is True:
        data = [(chat_id, "10:00", 1)]
        # Подготавливаем множественный запрос
        sql = "INSERT INTO notification (CHAT_ID, TIME, STATUS) values(?, ?, ?)"
        # Загружаем данные в базу
        cursor.executemany(sql, data)
        # Сохраняем изменения с помощью функции commit для объекта соединения
        conn.commit()
        # Просмотр данных
        data = cursor.execute("SELECT * FROM notification")
        for row in data:
            print(row)
        # Закрыть соединение с базой данных
        conn.close()
    else:
        print(f"такой есть уже {chat_id}")


def get_chat_id(chat_id: int, cursor):
    """
    Функция проверяет наличие записи в таблице, если запись есть возвращает его настройки
    :param int chat_id: chat id пользователя
    :return: tuple result: кортеж с данными записи о пользователе
    """
    # Формируем данные записи - почему нужно писать (chat_id,) я пока не понял, иначе не работает
    # cursor.execute("SELECT chat_id FROM notification WHERE chat_id = ?", (chat_id,))
    # if cursor.fetchone() is None:
    # ...
    # else:
    #     print(f"такой есть уже {chat_id}")
    #     conn.close()
    sql = f"SELECT chat_id FROM notification WHERE chat_id = {chat_id}"
    if cursor.execute(sql).fetchone() is None:
        return True
    else:
        return False

    # # Подготавливаем запрос
    # sql = f"SELECT * FROM notification WHERE chat_id = {chat_id}"
    # # Делаем запрос в базу данных
    # try:
    #     result = cursor.execute(sql).fetchone()
    #     return result
    # except:
    #     return "Записи с таким chat id нет"


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



conn = connect_db(LOCATION)
create_table(conn)
conn2 = connect_db(LOCATION)
create_chat_id(12312333, conn2)