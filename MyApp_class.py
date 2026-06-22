from kivy.app import App  # само приложение
from kivy.uix.boxlayout import BoxLayout  # способ структурирования
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.button import Button  # для создания кнопок
from kivy.uix.image import Image
import datetime

from DynamicLabel_class import DynamicLabel
from find_geo_weather import yandex_weather, ww_weather, geoposition
from one_day_data import one_day_data
from way_founder import way


# from kivy import Config                   # изменение размера окна
# Config.set("graphics", "weidth", "1400")
# Config.set("graphics", "height", "700")
# Config.write()

class MyApp(App):
    """
    Класс для создания приложения со всем интерфесом: Заголовок, 2 кнопки (погода на 1 и на 10 дней),
    ячейки с информацией о погоде (день недели, число + месяц, прогноз погоды, минимальная и максимальная
    температура дня).
    """
    running = True

    def __init__(self, **kwargs):
        """
        Инициализация базовых и общих параметров, которые всегда на виду.

        :param box_l_weather: list[BoxLayout] - Для создания списка из виджетов для цикличного изменения размера в
        зависимости от величины окна приложения
        :param scale: float - Динамический параметр для пропорционального изменения размера текста и картинок на экране.
        :param but_1: Button - Кнопка для отображения погоды на 1 день - на сегодня.
        :param but_10: Button - Кнопка для отображения погоды на 10 дней вперед.
        :param grid_l_1: GridLayout - Выделение пространства под отображение 10 ячеек с погодой.
        Разделение на 5 столбцов и 2 строки для компактного и ровного отображения на экране.
        :param title_label: DynamicLabel - Текстовый заголовок с погодой в конкретном городе, определенным по
        местоположению.
        """

        super().__init__(**kwargs)  # общедоступность всем функциям
        self.width, self.height = Window.size[0], Window.size[1]
        self.scale = 0.058 * (self.width ** 0.83 * self.height ** 0.1)
        self.box_l_weather: list[BoxLayout] = []

        self.but_1 = Button(text="Average weather for the day",
                            font_size=self.scale,
                            on_press=self.one_day_weather_button,
                            background_normal="",
                            background_color=(50 / 255, 164 / 255, 206 / 255, 1),
                            outline_width=1,
                            )
        self.but_10 = Button(text="Average weather for 10 days",
                             font_size=self.scale,
                             on_press=self.ten_days_weather_button,
                             background_normal="",
                             background_color=(88 / 255, 88 / 255, 88 / 255, 1),
                             outline_width=1,
                             )
        self.grid_l_1 = GridLayout(cols=5,  # столбцов кнопок
                                   col_default_width=10,
                                   pos_hint={"center_x": 0.5, "center_y": 1},
                                   size_hint=(1, 1),  # отношение к остальному
                                   padding=(0, 60, 0, 0),
                                   )
        self.title_label = DynamicLabel(text=f"[color=ffffff]Weather in {geoposition}[/color]",
                                        bold=True,  # выделение жирным
                                        text_size=(None, None),  # ширина возможного использования
                                        outline_width=2,
                                        size_hint_y=0.1,  # расположение сверху, займет 12% от экрана
                                        markup=True,  # для покраски текста
                                        )

    def build(self) -> AnchorLayout:
        """
        Функция, которая определяет границы отображения на экране, загружает фоновую картинку, создает кнопки.

        :return: anch_l_bg: AnchorLayout - Начальный экран с параметрами размещения объектов и с фоновой картинкой.
        """
        box_l_main = BoxLayout(orientation="vertical",
                               padding=(10, 10),  # отступ от верха
                               )

        box_l_main.add_widget(self.title_label)

        anch_l_1 = AnchorLayout(anchor_x="center",
                                anchor_y="top"
                                )
        box_l_1 = BoxLayout(orientation="horizontal",
                            size_hint=(1, 0.1),
                            )
        box_l_1.add_widget(self.but_1)
        box_l_1.add_widget(self.but_10)

        anch_l_1.add_widget(box_l_1)
        anch_l_1.add_widget(self.grid_l_1)
        box_l_main.add_widget(anch_l_1)
        box_l_main.bind(size=self.update_font_size)  # Привязываем изменение размера окна к методу update_font_size

        anch_l_bg = AnchorLayout(anchor_x="center", anchor_y="center")
        anch_l_bg.add_widget(Image(source=way + "Clouds_bg.png", size_hint=(2, 2)))
        anch_l_bg.add_widget(box_l_main)

        return anch_l_bg

    def one_day_weather_button(self, instance: Button) -> None:
        """
        Функция, стирающая всю имеющуюся картинку в приложении и создающая заново картинку с погодой на 1 день с
        изменением цвета кнопки 1-го дня для наглядности что выбрано. А также обновляется масштаб для текста и картинок.

        :param instance: Button - Передаваемый параметр в функцию. В функции не используется. Нужен для заглушки
        ошибки, что перессылаются дополнительные параметры. Не отправлять "Button" невозможно.
        :return: Созданный экран приложения с погодой на 1 день.
        """

        self.grid_l_1.clear_widgets()
        self.but_1.background_color = (50 / 255, 164 / 255, 206 / 255, 1)
        self.but_10.background_color = (88 / 255, 88 / 255, 88 / 255, 1)

        self.box_l_weather: list[BoxLayout] = []
        self.box_l_weather.append(BoxLayout(orientation="vertical",
                                            spacing=10,
                                            padding=(0, 40, 0, 50)
                                            ))
        self.box_l_weather[0].add_widget(one_day_data(yandex_data=yandex_weather, ww_data=ww_weather,
                                                      size_of_text=self.scale * 1.5,
                                                      number_of_day=datetime.datetime.today().day,
                                                      is_one_day=True))
        self.grid_l_1.add_widget(self.box_l_weather[0])

    def ten_days_weather_button(self, instance: Button) -> None:
        """
        Функция, стирающая всю имеющуюся картинку в приложении и создающая заново картинку с погодой на 10 дней с
        изменением цвета кнопки 10-го дня для наглядности что выбрано. Обновляется масштаб для текста и картинок на
        более мелкий, чтобы поместилось 10 объектов с погодой.

        :param instance: Button - Передаваемый параметр в функцию. В функции не используется. Нужен для заглушки
        ошибки, что перессылаются дополнительные параметры. Не отправлять "Button" невозможно.
        :return: Созданный экран приложения с погодой на 10 дней.
        """

        self.grid_l_1.clear_widgets()
        self.but_10.background_color = (50 / 255, 164 / 255, 206 / 255, 1)
        self.but_1.background_color = (88 / 255, 88 / 255, 88 / 255, 1)

        self.box_l_weather = []
        for id_date, date in enumerate(yandex_weather.keys()):
            self.box_l_weather.append(BoxLayout(orientation="vertical",
                                                spacing=10,
                                                padding=(0, 40, 0, 50)
                                                ))
            self.box_l_weather[id_date].add_widget(one_day_data(yandex_data=yandex_weather, ww_data=ww_weather,
                                                                size_of_text=self.scale,
                                                                number_of_day=date, is_one_day=False))
            self.grid_l_1.add_widget(self.box_l_weather[id_date])

    def update_font_size(self, *args: tuple) -> None:
        """
        Функция, принимающая на вход кортеж из контейнера BoxLayout с виджетами и параметрами размера экрана в пикселях.
        Функция изменяет масштаб заголовка, кнопок и ячеек с погодой в зависимости от размера окна приложения во
        избежание наслоения текста друг на друга. Не предотвращает наложение из-за чрезмерного уменьшения окна.

        :param args: tuple - (BoxLayout, [width, height]) - Параметр с шириной и высотой экрана, которые используются
        для вычисления нового масштаба для текста, кнопок и картинок.
        :return: Измененные параметры масштаба у title_label, but_1, but_10, title_label. Переделывает иконки с
        погодой под новый масштаб.
        """

        width, height = args[1]
        # Изменяем размер шрифта в зависимости от ширины окна
        # Пример: размер шрифта зависит от ширины и высоты окна
        self.scale = 0.058 * (width ** 0.83 * height ** 0.1)

        self.title_label.font_size = self.scale
        self.but_1.font_size = self.scale
        self.but_10.font_size = self.scale
        self.title_label.font_size = self.scale

        # Определение является ли ячейка для одного дня или для 10, что влияет на пересоздание их с учетом масштаба.
        if len(self.box_l_weather) == 1:
            numb_day_scale = 1.5
            is_one_day = True
        else:
            numb_day_scale = 1
            is_one_day = False

        box_l_weath = []
        self.grid_l_1.clear_widgets()  # Очистка экрана с ячейками погоды для предотвращения бесконечного их создания.
        for id_date, date in enumerate(zip(self.box_l_weather, yandex_weather.keys())):
            box_l_weath.append(BoxLayout(orientation="vertical",
                                         spacing=10,
                                         padding=(0, 40, 0, 50)
                                         ))
            box_l_weath[id_date].add_widget(one_day_data(yandex_data=yandex_weather, ww_data=ww_weather,
                                                         # accu_weather,
                                                         size_of_text=self.scale * numb_day_scale,
                                                         number_of_day=date[1], is_one_day=is_one_day))
            self.grid_l_1.add_widget(box_l_weath[id_date])

    def on_start(self) -> None:
        """
        Программное нажатие кнопки. Иначе без этого погода появится только после нажатия кнопки, что не очень удобно.
        """
        self.one_day_weather_button(self.but_1)

    def on_stop(self) -> None:
        """
        Функция для остановки работы программы при её закрытии, чтобы не тратила системные ресурсы.
        :return: Остановка через self.running = False без ошибок и продолжения работы в фоновом режиме.
        """
        self.running = False
