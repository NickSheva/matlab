"""Цель отобразить максимально приближенный рисунок к оригиналу"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D # creating custom lines

size = [40, 5, 5, 10, 10, 30]
labels = ["Работа", "Время с семьей", "Мероприятия, театры, рестораны",
          "Спорт", "Поездки", "Хобби"]
colors = ['dodgerblue', 'dimgrey', 'mediumorchid', 'red', 'gold', 'limegreen']
text_props = {'color': 'white', 'fontsize':10}
# Создаем рамку и холст
fig, ax = plt.subplots()
# Добавляем заголовок
plt.title(label="Copy table",
          pad=50,
          fontdict={'fontsize': 14,
                    'color': 'green'})
# создаем рисунок
ax.pie(x=size, labels=None, colors=colors, startangle=-55, autopct='%.f%%',
       textprops=text_props)

# Добавьте пользовательские данные отображение legend
legend_elements = [Line2D([0], [0], marker='o', markersize=10, lw=0, color='dodgerblue', label='Работа'),
                   Line2D([0], [0], marker='o', markersize=10, lw=0, color='red', label='Спорт'),
                   Line2D([0], [0], marker='o', markersize=10, lw=0, color='limegreen', label='Время с семьей'),
                   Line2D([0], [0], marker='o', markersize=10, lw=0, color='mediumorchid', label='Поездки'),
                   Line2D([0], [0], marker='o', markersize=10, lw=0, color='gold', label='Мероприятия, театры, рестораны'),
                   Line2D([0], [0], marker='o', markersize=10, lw=0, color='dimgrey', label='Хобби')]

ax.legend(handles=legend_elements, bbox_to_anchor=(1.3, 1.16), ncol=3, frameon=False)

plt.tight_layout()
# сохраниние графика
plt.savefig('copy.png')