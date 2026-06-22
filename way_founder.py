import os
import sys
from AppError_class import AppErrorPng


def way_found(relative_path: str) -> str:
    """
    Функция для сохранения пути до картинок с изображениями погоды и фоном с минимальной проверкой на наличие файлов.
    """

    try:
        # PyInstaller создает временную папку _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


way = way_found("Icon_of_weather\\png\\")

# Проверка на целостность
if not os.path.isfile(way + 'cl.png'):
    AppErrorPng().run()
    sys.exit()
