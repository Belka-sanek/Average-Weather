from MyApp_class import MyApp

"""
Функция, запускающая процесс создания приложения со средней погодой по региону местоположению.
"""
if __name__ == "__main__":
    MyApp().run()

# pip install pyinstaller
# pyinstaller --noconsole --add-data ".\\icon_of_weather\\png;icon_of_weather\\png" --icon=.\\icon_of_weather\\logo.ico --name=averageweather --onefile main.py

# pip install nuitka
# python -m nuitka --standalone --onefile --windows-disable-console --include-data-dir="icon_of_weather/png=icon_of_weather/png" --windows-icon-from-ico="icon_of_weather/logo.ico" --output-filename=averageweather main.py
