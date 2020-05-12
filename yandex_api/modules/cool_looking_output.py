from settings import conditions, weekdays, months, wind_directions, date_parts
from datetime import datetime


def cool_looking_weather_output(response_json):
    current_date = datetime.now()
    weekday = weekdays[current_date.weekday()]
    day = current_date.day
    month = months[current_date.month - 1]
    hour = current_date.hour
    print(get_greeting(hour))
    print(str(day)+ " " + month + ",  " + weekday)
    print("Сейчаc " + conditions[response_json["fact"]["condition"]])
    print("Температура воздуха состовляет: " + str(response_json['fact']['temp']) + "°C")
    print("По ощущениям: " + str(response_json['fact']['feels_like']) + "°C")
    print("Дождь пойдёт с вероятностью " + str(response_json["forecast"]["parts"][0]["prec_prob"]) +"%")
    print("Влажность воздуха состовляет: " + str(response_json['fact']['humidity'])+"%")
    print(wind_directions[response_json['fact']['wind_dir']] + " " + str(response_json['fact']['wind_speed'])+"м/с")
    print()

def future_weather_output(parts):
    for part in parts:
        print()
        print("Прогноз погоды на " + date_parts[part['part_name']])
        print("Температура воздуха составит от " + str(part['temp_min']) + "°C" + " до "
              + str(part['temp_min'])+ "°C")
        print("По ощущениям будет +- " + str(part['feels_like']) + "°C")
        print("Дождь будет идти с вероятностью " + str(part["prec_prob"]) +"%")
        print("Скорость ветра составит " + str(part['wind_gust']) + "м/с")


def get_greeting(current_hour):
    if (current_hour >= 23 or current_hour < 5): return("Доброй ночи!")
    elif (5 >= current_hour > 12): return("Доброе утро!")
    elif (12 >= current_hour > 6): return("Добрый день!")
    else: return("Добрый вечер!")
