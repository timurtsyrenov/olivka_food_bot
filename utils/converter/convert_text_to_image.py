from io import BytesIO

from data.config import FONT_LINK
from PIL import Image, ImageDraw, ImageFont


def convert_text_to_image(text: str) -> bytes:
    """
    Функция преобразует текст в изображение. Затем полученное изображение возвращает в виде
    потока байтов.
    :param str text: Преобразуемый текст
    :return bytes result_byte_image: Изображение в виде потока байтов
    """
    # Создаем пустое изображение размером 400х200, цвет фона: белый
    img = Image.open("utils/converter/background.webp")

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт и устанавливаем его размер
    font = ImageFont.truetype(FONT_LINK, 26)

    # Рисуем текст на изображении
    draw.text(xy=(20, 80), text=text, font=font, fill=(0, 0, 0))

    # Сохраняем и возвращаем изображение в виде потока байтов
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="WEBP")
    result_byte_image = img_byte_arr.getvalue()
    img_byte_arr.close()
    return result_byte_image
