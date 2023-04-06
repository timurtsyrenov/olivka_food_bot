from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def convert_text_to_image(text: str):
    """
    Функция преобразующая текст в изображение. Затем полученное изображение возвращает в виде
    потока байт.
    :param str text: преобразуемый текст
    :return BeautifulSoup soup: Страница сайта
    """
    # Создаем пустое изображение размером 400х200, цвет фона: белый
    img = Image.new("RGB", (400, 300), color=(255, 255, 255))

    # Создаем объект ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(img)

    # Загружаем шрифт и устанавливаем его размер
    font = ImageFont.truetype("arial.ttf", 15)

    # Рисуем текст на изображении
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    # Сохраняем и возвращаем изображение в виде потока байт
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='JPEG')
    result_byte_image = img_byte_arr.getvalue()
    return result_byte_image
