import sys

import requests
from bs4 import BeautifulSoup as BS
import datetime

from AppError_class import AppErrorOnSites

# Рабочая версия браузера, на которой тестировалось работоспособное приложение
header = {"User-Agent": "Opera/9.60 (Windows NT 10.0; U; en) Presto/2.1.1"}


def yandex_get_info(geoposition: str) -> dict:
    """
    Функция, которая берет погоду с сайта yandex.com по текущей геопозиции, а именно - городу нахождения.

    :param geoposition: str - город текущего местоположения
    :return: info_by_yandex: dict - информация с сайта с датой, днем недели, максимальной и минимальной температурой,
     id картинки прогноза погоды на 10 дней.
    """

    try:
        url_yandex = f"https://yandex.com/pogoda/en/{geoposition}"

        response_yandex = requests.get(url_yandex, headers=header)
        soup_yandex = BS(response_yandex.text, "lxml")  # "html.parser")
        data_yandex_day = soup_yandex.find_all("span", class_="AppShortForecastDay_title__2NpIg")
        data_yandex_date = soup_yandex.find_all("span", class_="AppShortForecastDay_subtitle__hv_2V")
        data_yandex_temp = soup_yandex.find_all("span", class_="AppShortForecastDay_temperature__DV3oM")
        data_yandex_temp = [int(data_yandex_temp[i].text.replace("−", "-").replace("°", ""))
                            for i in range(len(data_yandex_temp))]
        data_yandex_icon = soup_yandex.find_all("div",
                                                class_="style_weatherIcon__OE4YL AppShortForecastDay_icon__rlqHK")

        # Создание словаря с ключом по числам дней месяца, со значениями в виде списка из дня недели,
        # максимальной и минимальной температурой, id картинки прогноза погоды на 10 дней
        info_by_yandex = {}
        for day in range(len(data_yandex_day)):
            if data_yandex_date[day].text == "Today":
                info_by_yandex[datetime.datetime.today().day] = [
                    data_yandex_temp[day * 2], data_yandex_temp[day * 2 + 1],
                    data_yandex_day[day].text,
                    int(data_yandex_icon[day].get("style").lstrip("--icon:"))
                ]
            elif data_yandex_date[day].text.startswith("01"):
                info_by_yandex[1] = [data_yandex_temp[day * 2], data_yandex_temp[day * 2 + 1],
                                     data_yandex_day[day].text,
                                     int(data_yandex_icon[day].get("style").lstrip("--icon:"))]
            else:
                info_by_yandex[int(data_yandex_date[day].text)] = [data_yandex_temp[day * 2],
                                                                   data_yandex_temp[day * 2 + 1],
                                                                   data_yandex_day[day].text,
                                                                   int(data_yandex_icon[day].get("style").lstrip(
                                                                       "--icon:"))]
        if not info_by_yandex:
            print('Error in Yandex')
            AppErrorOnSites().run()
            sys.exit()

        return info_by_yandex

    except Exception as exc:
        print(exc)
        AppErrorOnSites().run()


def ww_get_info(geoposition: str) -> dict:
    """
    Функция, которая берет погоду с сайта world-weather.ru по текущей геопозиции, а именно - городу нахождения.

    :param geoposition: str - город текущего местоположения
    :return: info_by_ww: dict - информация с сайта с датой, максимальной и минимальной температурой на 10 дней.
    """

    try:
        url_ww = f"https://world-weather.ru/pogoda/russia/{geoposition}/month/"

        response_ww = requests.get(url_ww, headers=header)
        soup_ww = BS(response_ww.text, "lxml")  # "html.parser")
        data_ww_day = soup_ww.find_all("a")
        data_ww_dates = [int(data_ww_day[i].get("href")[-2:]) for i in range(19, 29)]
        ww_temp_list_end_week = [[int(soup_ww.find_all("a")[i].find("span").text.replace("°", "")),
                                  int(soup_ww.find_all("a")[i].find("p").text.replace("°", ""))] for i in range(19, 29)]

        # Создание словаря из 10 значений на 10 дней с ключом по числам дней месяца, со значениями в виде списка из
        # максимальной и минимальной температурой
        info_by_ww = {}
        for i, el in enumerate(data_ww_dates):
            info_by_ww[el] = [ww_temp_list_end_week[i][0], ww_temp_list_end_week[i][1]]

        if not info_by_ww:
            print('Error in World Weather')
            AppErrorOnSites().run()
            sys.exit()

        return info_by_ww

    except Exception as exc:
        print(exc)
        AppErrorOnSites().run()

# print(ww_get_info('Moscow'))
# print(yandex_get_info('Moscow'))
