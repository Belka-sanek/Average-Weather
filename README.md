# Average-Weather

Программа создана для иностранного заказчика, проживающего в России. 
Приложение выводит средние данные с разных метеостанций для города по текущему местоположению. 

*Требуется подключение к интернету и разрешение доступа к геопозиции.


The program was created for a foreign customer residing in Russia. 
The application outputs the average data from different weather stations for the city at the current location. 

*Requires an internet connection and permission to access the location.


Информация берется с сайтов https://yandex.ru/pogoda и https://world-weather.ru/pogoda

Information is taken from websites https://yandex.ru/pogoda and https://world-weather.ru/pogoda


Для компиляции десктоп приложения можно использовать консоль и библиотеку pyinstaller.

To compile a desktop application, you can use the console and the pyinstaller library.
* pip install pyinstaller
* pyinstaller --noconsole --add-data ".\\icon_of_weather\\png;icon_of_weather\\png" --icon=.\\icon_of_weather\\logo.ico --name=AverageWeather --onefile main.py
