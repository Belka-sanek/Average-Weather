import sys
from typing import Optional
import geocoder

from work_with_sites import yandex_get_info, ww_get_info
from AppError_class import AppErrorGeoposition, AppErrorCity, AppErrorInternetConnection, AppUnknownGeoError


def find_geoposition() -> Optional[str]:
    """
    Функция, которая находит местоположение устройства:
    название города, название региона, название страны в 2-символьном сокращении.
    Функция работает только с российским регионом из-за ограничений автоматизации поиска города на конкретных сайтах.
    :return: geoposition_find[0]: str - текст с названием города или
                                : None - если регион не найден или страна не Россия
    Если местоположение не найдено, то вызовет функцию для создания приложения,
    в окне которого выводится сообщение об ошибке.
    """

    geoposition_find = geocoder.ip('me')
    geoposition_list = str(geoposition_find)[24:-2].split(', ')

    if 'HTTPConnectionPool' in str(geoposition_find):
        AppErrorInternetConnection().run()
        sys.exit()
    elif geoposition_find.error:
        AppUnknownGeoError().run()
        sys.exit()
    try:
        if geoposition_list[2] == 'RU':
            return geoposition_list[0]
    except Exception as exc:
        print(exc)
        AppErrorGeoposition().run()
        sys.exit()


geoposition = find_geoposition()

try:
    """
    Функция для парсинга погоды с сайтов yandex.ru и world-weather.ru: dict.
    Если погода с сайтов не найдена или город не поддерживается на сайте, то вызовет ошибку; 
    тогда вызовет функцию для создания приложения, в окне которого выводится сообщение об ошибке.
    """
    yandex_weather = yandex_get_info(geoposition)
    ww_weather = ww_get_info(geoposition)

except Exception as exc:
    print(exc)
    AppErrorCity().run()
    sys.exit()
