from kivy.uix.label import Label              # Виджет для текста
from kivy.properties import NumericProperty   # для работы с динамично меняющимися данными

class DynamicLabel(Label):
    """
    Класс для создания слоя с текстом в виде заголовка над кнопками и картинками.
    font_size: NumericProperty - Свойство для хранения размера шрифта
    """
    font_size = NumericProperty(40)