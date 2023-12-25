"""Цель отобразить максимально приближенный рисунок к оригиналу"""
import matplotlib.pyplot as plt

size = [40, 5, 5, 10, 10, 30]
labels = ["Работа", "Время с семьей", "Мероприятия, театры, рестораны",
          "Спорт", "Поездки", "Хобби"]
colors = ['dodgerblue', 'dimgrey', 'mediumorchid', 'red', 'gold', 'limegreen']
text_props = {'color': 'white', 'fontsize':10}
# Создаем рамку и холст
fig, ax = plt.subplots()
# создаем рисунок
ax.pie(x=size, labels=None, colors=colors, startangle=-55, autopct='%.f%%',
       textprops=text_props)

ax.legend(labels, bbox_to_anchor=(1.1, 1.15), ncol=3)
plt.tight_layout()
# отобржаем на экране
plt.show()