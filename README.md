# 🥗 Olivka Food Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-2.25.1-green.svg)](https://docs.aiogram.dev/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://www.docker.com/)


---

## 📋 О проекте

**Olivka Food Bot** — это Telegram-бот, который автоматически парсит меню бизнес-ланчей с сайта [olivkafood.ru](https://olivkafood.ru) и предоставляет пользователям удобный доступ к актуальной информации о блюдах.

### ✨ Основные возможности

- 🍽️ **Просмотр меню** — получение полного меню бизнес-ланча на текущий день
- 📅 **Меню на сегодня** — быстрый доступ к актуальным предложениям
- 🔔 **Уведомления** — автоматическая рассылка меню по расписанию
- ⏰ **Настройка времени** — возможность установить удобное время получения уведомлений
- 🖼️ **Генерация изображений** — конвертация текстового меню в красивую картинку
- 👨‍💼 **Админ-панель** — уведомления администратору о запуске/остановке бота

---

## 🚀 Быстрый старт

### Требования

- Python 3.9 или выше
- [Poetry](https://python-poetry.org/) (рекомендуется) или pip
- Docker и Docker Compose (опционально)

### Установка зависимостей

```bash
# Клонируйте репозиторий
git clone https://github.com/timurtsyrenov/olivka_food_bot.git
cd olivka_food_bot

# Установите зависимости через Poetry
poetry install

# Или через pip
pip install -r requirements.txt  # если сгенерирован
```
### Создание .env

```bash
Копируется .env_EXAMPLE
BOT_TOKEN - Токен можно получить у телеграмм бота https://t.me/BotFather
ADMIN_ID - можно узнать https://t.me/chatIDrobot
FONT_LINK - Путь до файла со шрифтом на Windows достаточно указать название шрифта, в linux полный путь example: "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
LOG_LEVEL - Уровень логирования приложения, по умолчанию выставляется DEBUG
MIDDLEWARE_BAN - Количество секунд бана, в случае спама бота
```
---

## 🐳 Запуск через Docker

### Сборка и запуск контейнеров

```bash
docker-compose up -d --build
```
---


👥 Авторы
Timur Tsyrenov — timurtsyrenov
Vadim V. — enohpi

