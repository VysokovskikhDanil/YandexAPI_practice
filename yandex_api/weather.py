# -*- coding: utf-8 -*-
from yandex_weather_api import get_weather_by_lat_lon
from cool_looking_output import cool_looking_weather_output, future_weather_output
from local_memory import weather_response
from datetime import datetime
from pathlib import Path
import sys


def update_weather():
    file_path = Path("./") / "local_memory.py"
    if(weather_response.get("status", 300) == 403 or int(datetime.now().timestamp()) - weather_response["now"] > 30 * 60):
        local_memory = open(file_path, "w+")
        local_memory.write("weather_response = " + str(get_weather_by_lat_lon('56.841238', '60.615093')))
        local_memory.close()

if(sys.argv[-1] in ['help', '-h', '--help', '?']): print("Чтобы начать пользоваться этой программой, просто запустите её :)")
else:
    update_weather()
    cool_looking_weather_output(weather_response)
    print("Хотите узнать прогноз погоды на ближайшее время?")
    while (True):
        user_input = input("Ваш ответ[Да/Нет]: ")
        if (user_input.lower() in ["да", "yes"]):
            future_weather_output(weather_response['forecast']['parts'])
            break
        elif(user_input.lower() in ["нет", "no"]):
            print("Окей, закрываюсь")
            break
        else: print("Мы не поняли, давай попробуем ещё раз.")
