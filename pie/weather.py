"""Work with csv file"""
import csv
from pathlib import Path

filename = Path('weather/sitka_weather_07-2018_simple.csv')
if filename.is_file() and filename.suffix == '.csv':
    print("Yes")
else:
    print("No")
