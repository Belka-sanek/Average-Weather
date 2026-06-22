import os
import sys

from kivy.app import App  # само приложение
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.image import Image

from DynamicLabel_class import DynamicLabel


def layout_creator(text: str) -> AnchorLayout:
    """
    Функция для создания приложения, в окне которого выводится сообщение об ошибке.
    :param text: str - сообщение об ошибке, переданная извне
    :return: окно приложения с ошибкой, переданной из text
    """
    layout = AnchorLayout(anchor_x="center", anchor_y="center")
    title_geo_error = DynamicLabel(text=f"[color=ff0000]{text}[/color]",
                                   font_size=Window.size[0] / 20,  # размер текста
                                   padding=(0, 0, 0, 10),
                                   outline_width=2,
                                   bold=True,  # выделение жирным
                                   size_hint_y=0.2,  # расположение сверху, займет 20% от ячейки
                                   markup=True,  # для покраски текста
                                   valign="center", halign="center",
                                   )
    try:
        # PyInstaller создает временную папку _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    way = os.path.join(base_path, "Icon_of_weather\\png\\")

    layout.add_widget(Image(source=way + "Clouds_bg.png", size_hint=(2, 2)))
    layout.add_widget(title_geo_error)

    return layout


class AppErrorGeoposition(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение об ошибке,
    что не нашлось Ваше местоположение.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о ненайденном местоположении
        """
        text = 'Error in finding your position'
        return layout_creator(text)


class AppErrorCity(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение об ошибке,
    что на сайте погоды не нашелся Ваш город.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о ненайденном городе.
        """
        text = 'Error in searching a city for weather'
        return layout_creator(text)


class AppErrorPng(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение об ошибке,
    что в папке нет нужных файлов.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о ненайденном файле.
        """
        text = 'Error in png finding'
        return layout_creator(text)


class AppErrorInternetConnection(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение об ошибке подключения
    к интернету.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о неудачном подключении к интернету.
        """
        text = 'Error internet connection'
        return layout_creator(text)


class AppUnknownGeoError(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение об ошибке подключения
    к интернету.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о неудачном подключении к интернету.
        """
        text = 'Unknown geoposition error'
        return layout_creator(text)

class AppErrorOnSites(App):
    """
    Класс для создания приложения, в окне которого выводится сообщение о сторонней ошибке
    на сайте поиска погоды.
    """

    def build(self) -> App:
        """
        Функция, которая передает:
        text: str - информацию о классе ошибки
        в функцию layout_creator
        :return: окно приложения с ошибкой о неудачном подключении к интернету.
        """
        text = 'Error on the weather website'
        return layout_creator(text)
