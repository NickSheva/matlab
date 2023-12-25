"""Work with csv file"""
import csv
from pathlib import Path


filename = Path('weather/sitka_weather_07-2018_simple.csv')
# reading CSV file

if filename.is_file() and filename.suffix == '.csv':
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        print('\n'.join(f"{i} {value}" for i, value in enumerate(header)))
        highs, lows = [], []
        for row in reader:
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
        print(highs)
        print(lows)

else:
    print("No")
