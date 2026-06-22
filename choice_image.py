import datetime
from kivy.uix.image import Image

from way_founder import way

names_image = ['cl.png',  # 0
               'cl_ra.png',  # 1
               'cl_sn.png',  # 2
               'cl_ra_sn.png',  # 3
               'cl_ts_ra.png',  # 4
               'sun_d.png',  # 5
               'sun_n.png',  # 6
               'sun_cl_d.png',  # 7
               'sun_cl_n.png',  # 8
               'sun_cl_ra_d.png',  # 9
               'sun_cl_ra_n.png',  # 10
               'sun_cl_sn_d.png',  # 11
               'sun_cl_sn_n.png']  # 12


def choice_image_one_day(one_day_img: int):
    """
    Функция, принимающая на вход id картинки с сайта yandex.ru по номеру дня.
    Определятся какое изображение следует вернуть по id в зависимости от погоды и времени суток.

    :param one_day_img: int - id с номером погоды, созданный на основе сайта yandex.ru
    :return: image: Image - класс kivy, возвращающий изображения с погодой и осадками
    """

    hour_now = datetime.datetime.today().hour

    if one_day_img == 25:
        name_image = names_image[0]  # облака, туман

    elif 12 <= one_day_img <= 14:
        name_image = names_image[1]  # дождь
    elif 15 <= one_day_img <= 17 or one_day_img == 19:
        name_image = names_image[2]  # снег, град
    elif one_day_img == 18:
        name_image = names_image[3]  # мокрый снег

    elif 20 <= one_day_img <= 22:
        name_image = names_image[4]  # гроза + сухо, дождь, град

    elif 26 <= one_day_img <= 27:
        if 6 <= hour_now < 21:
            name_image = names_image[5]  # солнце
        else:
            name_image = names_image[6]  # ночь

    elif 23 <= one_day_img <= 24:
        if 6 <= hour_now < 21:
            name_image = names_image[7]  # облака днем
        else:
            name_image = names_image[8]  # облака ночью

    elif (0 <= one_day_img <= 2 or
          29 <= one_day_img <= 31 or
          6 <= one_day_img <= 8 or
          35 <= one_day_img <= 37):
        if 6 <= hour_now or hour_now < 21:
            name_image = names_image[9]  # дождь днем
        else:
            name_image = names_image[10]  # дождь ночью

    elif (3 <= one_day_img <= 5 or
          32 <= one_day_img <= 34 or
          9 <= one_day_img <= 11 or
          38 <= one_day_img <= 40):
        if 6 <= hour_now < 21:
            name_image = names_image[11]  # снег днем
        else:
            name_image = names_image[12]  # снег ночью

    else:
        name_image = names_image[0]

    image = Image(source=way + name_image,
                  size_hint=(0.4, 0.3),
                  pos_hint={"center_x": 0.5, "center_y": 0.5},
                  )
    return image
