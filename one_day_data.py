import datetime
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from DynamicLabel_class import DynamicLabel
from choice_image import choice_image_one_day


def one_day_data(yandex_data: dict, ww_data: dict,
                 size_of_text: float = 30.0,
                 number_of_day: int = 1,
                 is_one_day: bool = True) -> BoxLayout:
    """
    Функция для создания блока одного дня погоды. Она включает в себя:
    вывод дня недели, даты, изображения с прогнозом погоды, максимальной и минимальной температуры дня.
    Средняя температура рассчитывается исходя из среднего значения с разных сайтов.
    В моем случае с yandex.ru и world-weather.ru

    :param yandex_data: dict - словарь с датой, id картинок, максимальной и минимальной температурой
    :param ww_data: dict - словарь с датой, максимальной и минимальной температурой
   #:param accu_data: dict - резервный словарь с датой, id картинок, максимальной и минимальной температурой
    для реализации среднего с 3-х и более сайтов с погодой. Не используется в связи с невозможностью автоматизировать
    поиск погоды по городам на этом сайте.

    :param size_of_text: float - индивидуальный параметр ячейки с текстом для каждого конкретного текста.
    Изменяется в зависимости от величины открытого окна и при обновлении страницы путем нажаия на кнопки.

    :param number_of_day: int - дата конкретного дня без месяца и года. Нужен для ориентирования и выбора нужных
    значений из словарей yandex_data, ww_data и accu_data.

    :param is_one_day: bool - True - если погода выводится для одного дня, то название дня недели выводится целиком.
                            False - если погода выводится для нескольких дней, то название дня недели выводится кратко,
                            если размер экрана ниже 700 пикселей (когда идет наложение текста друг на друга.

    :return: box_l_one_day_data: BoxLayout - возвращает готовую ячейку с текстом, температурой и картинкой погоды.
    """
    box_l_one_day_data = BoxLayout(orientation="vertical",
                                   padding=(0, 10, 0, 20),  # отступ от краев
                                   size_hint=(1, 0.9),
                                   )
    day_day_temp = round(
        (yandex_data[number_of_day][0] + ww_data[number_of_day][0]) / 2)
    night_day_temp = round(
        (yandex_data[number_of_day][1] + ww_data[number_of_day][1]) / 2)

    year = datetime.datetime.today().year
    if number_of_day - datetime.datetime.today().day >= 0:
        month = datetime.datetime.today().strftime(".%m")
    else:
        month = datetime.datetime.today().month + 1
        if 10 <= month <= 12:
            month = '.' + str(month)
        else:
            month = '.0' + str(month % 12)
            year = datetime.datetime.today().year + 1

    if Window.size[0] > 700 or is_one_day:
        day_of_week = datetime.datetime(year, int(month[1:]), number_of_day).strftime("%A")
        text_temp = """[color=ffffff]Max: {0}°\nMin: {1}°[/color]""".format(day_day_temp, night_day_temp)
    else:
        day_of_week = yandex_data[number_of_day][2]
        text_temp = """[color=ffffff]{0}°\n{1}°[/color]""".format(day_day_temp, night_day_temp)

    lbl_day_of_week = DynamicLabel(
        text="""[color=ffffff]{0}\n{1}[/color]""".format(day_of_week, str(number_of_day) + month),
        font_size=size_of_text,  # размер текста
        padding=(0, 0, 0, 10),
        outline_width=2, # толщина обводки в пикселях
        bold=True,  # выделение жирным
        size_hint_y=0.2,  # расположение сверху, займет 20% от ячейки
        markup=True,  # для покраски текста
        valign="top", halign="center",
    )
    lbl_day_temp = DynamicLabel(
        text=text_temp,
        padding=(0, 50, 0, 20),
        font_size=size_of_text ** 0.9,  # размер текста
        outline_width=2,
        bold=True,  # выделение жирным
        size_hint_y=0.08,  # расположение сверху, займет 20% от ячейки
        markup=True,  # для покраски текста
        valign="top", halign="center",
    )

    box_l_one_day_data.add_widget(lbl_day_of_week)
    box_l_one_day_data.add_widget(choice_image_one_day(yandex_data[number_of_day][3]))
    box_l_one_day_data.add_widget(lbl_day_temp)

    return box_l_one_day_data
