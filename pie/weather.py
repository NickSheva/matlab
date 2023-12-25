"""Work with csv file"""
import csv
import matplotlib.pyplot as plt

filename = 'weather/sitka_weather_07-2018_simple.csv'

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
    # Нанесение данных на диаграмму.
    plt.style.use('seaborn-v0_8-paper')
    fig, ax = plt.subplots()
    ax.plot(highs, c='r', alpha=.5)
    ax.plot(lows, c='b', alpha=.5)
    ax.set_title("Daily high temperatures, July 2018", fontsize=20, color='thistle')
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16, c='rosybrown')
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.set_ylim(40,80)
    plt.show()

