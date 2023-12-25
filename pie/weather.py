"""Work with csv file"""
import csv
from pathlib import Path

filename = Path('weather/sitka_weather_07-2018_simple.csv')
if filename.is_file() and filename.suffix == '.csv':
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        print('\n'.join(f"{i} {value}" for i, value in enumerate(header)))

else:
    print("No")
