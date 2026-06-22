from MyApp_class import MyApp

"""
Функция, запускающая процесс создания приложения со средней погодой по региону местоположению.
"""
if __name__ == "__main__":
    MyApp().run()

# pyinstaller --noconsole --add-data ".\\icon_of_weather\\png;icon_of_weather\\png" --icon=.\\icon_of_weather\\logo.ico --name=averageweather --onefile main.py
