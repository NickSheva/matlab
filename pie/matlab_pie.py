"""Цель отобразить максимально приближенный рисунок к оригиналу"""
import matplotlib.pyplot as plt

size = [40, 5, 5, 10, 10, 30]
labels = ["Работа", "Время с семьей", "Мероприятия, театры, рестораны",
          "Спорт", "Поездки", "Хобби"]
colors = ['dodgerblue', 'dimgrey', 'mediumorchid', 'red', 'gold', 'limegreen']
# Создаем рамку и холст
fig, ax = plt.subplots()
# создаем рисунок
ax.pie(x=size, labels=labels, colors=colors)
# отобржаем на экране
plt.show()