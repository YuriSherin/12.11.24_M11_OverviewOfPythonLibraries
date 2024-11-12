"""
Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy,
matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями
и функциями. К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
            https://requests.readthedocs.io/en/latest/index.html
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение)
        и вывести результаты в консоль.
            https://pandas.pydata.org/docs/user_guide/index.html
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
            https://numpy.org/doc/stable/user/absolute_beginners.html
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
            https://matplotlib.org/stable/users/explain/quick_start.html
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
            https://pillow.readthedocs.io/en/stable/

В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам
выбранная библиотека и как вы расширили возможности Python с её помощью.

Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
"""
import json
from pprint import pprint

import matplotlib.pyplot as plt
import requests
from PIL import Image, ImageFilter, ImageGrab


# ============ ИСПОЛЬЗОВАНИЕ БИБЛИОТЕКИ Pillow =====================================
def resize_image(filename: str, width, height):
    """Функция открывает указанный файл, изменяет его размер и сохраняет измененный файл"""
    with Image.open(filename) as image:
        print(f'Old size image: {image.size}')
        image = image.resize((width, height))
        print(f'New size image: {image.size}')
        image.save(f'resize_image_{filename}')


def filter_image(filename):
    """Функция открывает указанный файл, конвертирует изображение в черно-белый цвет,
    сглаживает изображение фильтром ImageFilter.SMOOTH и идентифицирует границы изображения
     фильтром ImageFilter.FIND_EDGES и сохраняет изображение в файле"""
    with Image.open(filename) as image:
        image = image.convert('L')
        image = image.filter(ImageFilter.SMOOTH)
        image = image.filter((ImageFilter.FIND_EDGES))
        image.save(f'filter_{filename}')


def screenshot_image(filename):
    """Функция создает скрин-шот дисплея и сохраняет изображение в файл"""
    screenshot = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)
    screenshot.save(filename)


# ================ ИСПОЛЬЗОВАНИЕ БИБЛИОТЕКИ matplotlib.pyplot =======================
def building_parabola(x_data: list, y_data: list):
    """Функция строит график квадратичной параболы,
    а также выводит название графика и подписывает оси X и Y"""
    plt.title('Парабола y = X**2:')
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.grid()
    plt.plot(x_data, y_data)
    plt.show()


def number_of_days_in_month(months, days):
    """Функция строит вертикальную столбчатую диаграмму зависимости
    количества дней от месяца года"""
    plt.bar(months, days)
    plt.title('Количество дней в месяце:')
    plt.xlabel('месяц')
    plt.ylabel('дней')
    plt.xticks(rotation=90)
    plt.show()


# ================== ИСПОЛЬЗОВАНИЕ БИБЛИОТЕКИ requests ========================
def get_requests(url: str):
    """Функция получает данных о курсах валют с сайта на текущую дату.
    Полученные данные выводятся в консоль в формате json и сохраняются в файл
    в формате json"""
    r_data = requests.get(url)
    if r_data.ok:
        try:
            r_data = r_data.json()
        except requests.exceptions.JSONDecodeError as e:
            print('Содержимое ответа не в формате json.',
                  'От источника был получен следующий ответ:', r_data, sep='\n')
        else:
            pprint(r_data['Valute'])
            with open('data_valute.json', 'w', encoding='utf8') as file:
                json.dump(r_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    """Вызов функций для работы с изображениями методами библиотеки Pillow
    Последовательно вызывается пользовательские функции
    для изменения размера изображения, размытия и определения границ изображения и
    для создания скрин шота дисплея"""
    resize_image('Золотая осень 4.jpg', 800, 600)
    filter_image('Золотая осень 4.jpg')
    screenshot_image('screenshot_display.jpg')

    # ==========================================================================

    """Вызов функций для построения графиков методами библиотеки matplotlib.pylib
    а именно: построение графика квадратичной параболы и построение столбчатой
    диаграммы зависимости количества дней в каждом месяце года"""
    x_data = [x for x in range(-5, 6)]  # X
    y_data = [y ** 2 - 10 for y in range(-5, 6)]  # Y
    building_parabola(x_data, y_data)

    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
              'сентябрь', 'октябрь', 'ноябрь', 'декабрь']  # X
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Y
    number_of_days_in_month(months, days)

    # ===============================================================================

    """Использование модуля requests для получения данных о курсах валют с сайта 
    на текущую дату. Полученные данные выводятся в консоль в формате json и
    сохраняются в файл в формате json."""

    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    get_requests(URL)
