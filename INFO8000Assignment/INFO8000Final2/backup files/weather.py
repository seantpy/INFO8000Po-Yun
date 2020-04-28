{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter city: Athens\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://api.openweathermap.org/data/2.5/forecast?q=Athens&appid=8f2980aea5484e2d60be6e013e5c0fda\n",
      "{'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1587319200, 'main': {'temp': 291.02, 'feels_like': 289.96, 'temp_min': 291.02, 'temp_max': 291.4, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1005, 'humidity': 57, 'temp_kf': -0.38}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.29, 'deg': 174}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-19 18:00:00'}, {'dt': 1587330000, 'main': {'temp': 289.97, 'feels_like': 289.36, 'temp_min': 289.97, 'temp_max': 290.26, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1005, 'humidity': 63, 'temp_kf': -0.29}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 66}, 'wind': {'speed': 0.84, 'deg': 172}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-19 21:00:00'}, {'dt': 1587340800, 'main': {'temp': 289.32, 'feels_like': 289.04, 'temp_min': 289.32, 'temp_max': 289.51, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 64, 'temp_kf': -0.19}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'clouds': {'all': 44}, 'wind': {'speed': 0.22, 'deg': 225}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-20 00:00:00'}, {'dt': 1587351600, 'main': {'temp': 288.65, 'feels_like': 288.13, 'temp_min': 288.65, 'temp_max': 288.75, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1003, 'humidity': 66, 'temp_kf': -0.1}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 61}, 'wind': {'speed': 0.49, 'deg': 119}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-20 03:00:00'}, {'dt': 1587362400, 'main': {'temp': 290.43, 'feels_like': 289.78, 'temp_min': 290.43, 'temp_max': 290.43, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 74}, 'wind': {'speed': 0.88, 'deg': 118}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-20 06:00:00'}, {'dt': 1587373200, 'main': {'temp': 292.27, 'feels_like': 290.79, 'temp_min': 292.27, 'temp_max': 292.27, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1005, 'humidity': 55, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 97}, 'wind': {'speed': 2.12, 'deg': 142}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-20 09:00:00'}, {'dt': 1587384000, 'main': {'temp': 292.41, 'feels_like': 290.58, 'temp_min': 292.41, 'temp_max': 292.41, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 97}, 'wind': {'speed': 3.3, 'deg': 148}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-20 12:00:00'}, {'dt': 1587394800, 'main': {'temp': 291.39, 'feels_like': 290.02, 'temp_min': 291.39, 'temp_max': 291.39, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1003, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 97}, 'wind': {'speed': 2.94, 'deg': 153}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-20 15:00:00'}, {'dt': 1587405600, 'main': {'temp': 290.57, 'feels_like': 290.18, 'temp_min': 290.57, 'temp_max': 290.57, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 98}, 'wind': {'speed': 1.58, 'deg': 144}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-20 18:00:00'}, {'dt': 1587416400, 'main': {'temp': 290.78, 'feels_like': 291.18, 'temp_min': 290.78, 'temp_max': 290.78, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1005, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.36, 'deg': 78}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-20 21:00:00'}, {'dt': 1587427200, 'main': {'temp': 289.91, 'feels_like': 288.66, 'temp_min': 289.91, 'temp_max': 289.91, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.44, 'deg': 356}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-21 00:00:00'}, {'dt': 1587438000, 'main': {'temp': 288.74, 'feels_like': 286.25, 'temp_min': 288.74, 'temp_max': 288.74, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 68}, 'wind': {'speed': 4.34, 'deg': 358}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-21 03:00:00'}, {'dt': 1587448800, 'main': {'temp': 289.37, 'feels_like': 285.38, 'temp_min': 289.37, 'temp_max': 289.37, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1003, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 70}, 'wind': {'speed': 6.06, 'deg': 1}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-21 06:00:00'}, {'dt': 1587459600, 'main': {'temp': 291.45, 'feels_like': 287.23, 'temp_min': 291.45, 'temp_max': 291.45, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 93}, 'wind': {'speed': 6.35, 'deg': 8}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-21 09:00:00'}, {'dt': 1587470400, 'main': {'temp': 292.34, 'feels_like': 286.57, 'temp_min': 292.34, 'temp_max': 292.34, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1003, 'humidity': 56, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 47}, 'wind': {'speed': 8.38, 'deg': 16}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-21 12:00:00'}, {'dt': 1587481200, 'main': {'temp': 289.9, 'feels_like': 283.52, 'temp_min': 289.9, 'temp_max': 289.9, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1002, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 22}, 'wind': {'speed': 9.05, 'deg': 14}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-21 15:00:00'}, {'dt': 1587492000, 'main': {'temp': 287.26, 'feels_like': 280.66, 'temp_min': 287.26, 'temp_max': 287.26, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1003, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 56}, 'wind': {'speed': 8.94, 'deg': 3}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-21 18:00:00'}, {'dt': 1587502800, 'main': {'temp': 286.33, 'feels_like': 279.83, 'temp_min': 286.33, 'temp_max': 286.33, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 81}, 'wind': {'speed': 8.63, 'deg': 359}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-21 21:00:00'}, {'dt': 1587513600, 'main': {'temp': 285.78, 'feels_like': 279.45, 'temp_min': 285.78, 'temp_max': 285.78, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1004, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 82}, 'wind': {'speed': 8.21, 'deg': 360}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-22 00:00:00'}, {'dt': 1587524400, 'main': {'temp': 285.39, 'feels_like': 279.03, 'temp_min': 285.39, 'temp_max': 285.39, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1004, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 8.26, 'deg': 357}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-22 03:00:00'}, {'dt': 1587535200, 'main': {'temp': 285.58, 'feels_like': 277.97, 'temp_min': 285.58, 'temp_max': 285.58, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1006, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 9.98, 'deg': 11}, 'rain': {'3h': 0.18}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-22 06:00:00'}, {'dt': 1587546000, 'main': {'temp': 286.72, 'feels_like': 277.85, 'temp_min': 286.72, 'temp_max': 286.72, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1007, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 91}, 'wind': {'speed': 11.56, 'deg': 8}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-22 09:00:00'}, {'dt': 1587556800, 'main': {'temp': 286.95, 'feels_like': 277.08, 'temp_min': 286.95, 'temp_max': 286.95, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 82}, 'wind': {'speed': 12.92, 'deg': 8}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-22 12:00:00'}, {'dt': 1587567600, 'main': {'temp': 286.07, 'feels_like': 277.08, 'temp_min': 286.07, 'temp_max': 286.07, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 74}, 'wind': {'speed': 11.62, 'deg': 4}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-22 15:00:00'}, {'dt': 1587578400, 'main': {'temp': 285.63, 'feels_like': 278.48, 'temp_min': 285.63, 'temp_max': 285.63, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 65, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 85}, 'wind': {'speed': 8.93, 'deg': 359}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-22 18:00:00'}, {'dt': 1587589200, 'main': {'temp': 285.51, 'feels_like': 279.69, 'temp_min': 285.51, 'temp_max': 285.51, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 67, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 69}, 'wind': {'speed': 7.13, 'deg': 358}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-22 21:00:00'}, {'dt': 1587600000, 'main': {'temp': 285.13, 'feels_like': 278.66, 'temp_min': 285.13, 'temp_max': 285.13, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 82}, 'wind': {'speed': 7.75, 'deg': 6}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-23 00:00:00'}, {'dt': 1587610800, 'main': {'temp': 284.01, 'feels_like': 278.08, 'temp_min': 284.01, 'temp_max': 284.01, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 80}, 'wind': {'speed': 6.8, 'deg': 3}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-23 03:00:00'}, {'dt': 1587621600, 'main': {'temp': 285.01, 'feels_like': 278, 'temp_min': 285.01, 'temp_max': 285.01, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 62, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 90}, 'wind': {'speed': 8.36, 'deg': 5}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-23 06:00:00'}, {'dt': 1587632400, 'main': {'temp': 286.77, 'feels_like': 279.34, 'temp_min': 286.77, 'temp_max': 286.77, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1009, 'humidity': 56, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 87}, 'wind': {'speed': 9.01, 'deg': 8}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-23 09:00:00'}, {'dt': 1587643200, 'main': {'temp': 287.48, 'feels_like': 279.07, 'temp_min': 287.48, 'temp_max': 287.48, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1009, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 84}, 'wind': {'speed': 10.45, 'deg': 10}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-23 12:00:00'}, {'dt': 1587654000, 'main': {'temp': 286.5, 'feels_like': 278.24, 'temp_min': 286.5, 'temp_max': 286.5, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 53, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 88}, 'wind': {'speed': 9.91, 'deg': 13}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-23 15:00:00'}, {'dt': 1587664800, 'main': {'temp': 285.16, 'feels_like': 278.9, 'temp_min': 285.16, 'temp_max': 285.16, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1008, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 94}, 'wind': {'speed': 6.79, 'deg': 0}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-23 18:00:00'}, {'dt': 1587675600, 'main': {'temp': 284.32, 'feels_like': 277.65, 'temp_min': 284.32, 'temp_max': 284.32, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 59, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'clouds': {'all': 39}, 'wind': {'speed': 7.5, 'deg': 350}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-23 21:00:00'}, {'dt': 1587686400, 'main': {'temp': 284.34, 'feels_like': 277.49, 'temp_min': 284.34, 'temp_max': 284.34, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1008, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 62}, 'wind': {'speed': 8.07, 'deg': 352}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-24 00:00:00'}, {'dt': 1587697200, 'main': {'temp': 283.92, 'feels_like': 276.93, 'temp_min': 283.92, 'temp_max': 283.92, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 65, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 4}, 'wind': {'speed': 8.22, 'deg': 356}, 'sys': {'pod': 'n'}, 'dt_txt': '2020-04-24 03:00:00'}, {'dt': 1587708000, 'main': {'temp': 285.81, 'feels_like': 276.75, 'temp_min': 285.81, 'temp_max': 285.81, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 55, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 12}, 'wind': {'speed': 11.02, 'deg': 6}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-24 06:00:00'}, {'dt': 1587718800, 'main': {'temp': 288.09, 'feels_like': 278.74, 'temp_min': 288.09, 'temp_max': 288.09, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 47, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 23}, 'wind': {'speed': 11.4, 'deg': 9}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-24 09:00:00'}, {'dt': 1587729600, 'main': {'temp': 288.69, 'feels_like': 279.66, 'temp_min': 288.69, 'temp_max': 288.69, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1007, 'humidity': 48, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 17}, 'wind': {'speed': 11.17, 'deg': 15}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-24 12:00:00'}, {'dt': 1587740400, 'main': {'temp': 287.91, 'feels_like': 279.65, 'temp_min': 287.91, 'temp_max': 287.91, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1006, 'humidity': 49, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 39}, 'wind': {'speed': 9.95, 'deg': 12}, 'sys': {'pod': 'd'}, 'dt_txt': '2020-04-24 15:00:00'}], 'city': {'id': 264371, 'name': 'Athens', 'coord': {'lat': 37.9795, 'lon': 23.7162}, 'country': 'GR', 'population': 729137, 'timezone': 10800, 'sunrise': 1587267822, 'sunset': 1587315857}}\n"
     ]
    }
   ],
   "source": [
    "import json, requests, pprint\n",
    "\n",
    "\n",
    "city = input (\"Enter city:\")\n",
    "base_url = \"http://api.openweathermap.org/data/2.5/forecast\"\n",
    "aapid = \"8f2980aea5484e2d60be6e013e5c0fda\"\n",
    "url = f'{base_url}?q={city}&appid={aapid}'\n",
    "print(url)\n",
    "if city != '':\n",
    "    r = requests.get(url)\n",
    "    print(r.json())\n",
    "    #http://api.openweathermap.org/data/2.5/forecast?q=Athens&appid=8f2980aea5484e2d60be6e013e5c0fda\n",
    "    #http://api.openweathermap.org/data/2.5/forecast?q=Athens&aapid=8f2980aea5484e2d60be6e013e5c0fda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}