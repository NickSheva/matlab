"""Создание аналогичного изобржения с помощью
инструментов  библиотеки matplotlib"""

#  импортируем зависимости
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Указываем данные для переменных
sizes = [554.6, 822.6]
labels = ['Чистый прирост\n стоимости', 'Дивиденды (с\n учетом налогов)']
colors = ['mediumseagreen', 'gold']
# устанавливаем данные для пирога (край, ширина линии и стиль)
wedgeprops = {'edgecolor': 'white', 'linewidth': 2, 'linestyle': '-'}
# устанавливаем данные для текста (цвет, рашмер и стиль шрифта)
textprops = {'color': 'black', 'size': 16, 'weight': 'bold'}
# установливаем рамку, на которой мы не можем рисовать
# в одной записной книжке или скрипте может быть несколько фигур.
# у каждого рисунка может быть несколько подсюжетов.
# здесь подсюжет является синонимом осей.
# но мы можем задавать размер и цвет для рамки
fig = plt.figure(facecolor='black', figsize=(8, 7))
# ax, сокращенно от оси, - это холст, на котором вы рисуете.
ax = fig.add_subplot()
# рисуем пирог с переменными(size, labels, colors)
# устанавливаем autopct в процентах и расположение в пироге с помощью pctdistance
# крутим пирог на 90 градусов с помощью startangle
# устанавливаем radius, увеличивая или уменьшая пирог
# вращаем labels с помощью  rotatelabels=True и дистанцию
patches, texts, autotexts = ax.pie(sizes, colors=colors,
       autopct='%.2f%%', pctdistance=.4,
       startangle=90,
       radius=1.2,
       rotatelabels=True, labeldistance=0.95,
       wedgeprops=wedgeprops,
       textprops=textprops)
# Добавляем пользовательские данные отображение legend
fig.add_artist(Line2D([0.62], [0.64], marker='s', markersize=16, lw=0, color='gold',
                      markeredgecolor='white', markeredgewidth=3))
fig.add_artist(Line2D([0.62], [0.4], marker='s', markersize=16, lw=0, color='mediumseagreen',
                      markeredgecolor='white', markeredgewidth=3))
# Adding text without box on the plot.
ax.text(1.8, .48, 'Чистый прирост\n стоимости', color='w', size=18, weight='bold')
ax.text(1.8, -.64, 'Дивиденды (с\n учетом налогов)', color='w', size=18, weight='bold')
# устанавливаем даные для legend
# fig.legend(labels, bbox_to_anchor=(1.0, 0.7), labelcolor='white',
#            prop={'weight': 'bold', 'size': 18}, labelspacing = 4, frameon=False)
# назначаем место для пирога
plt.subplots_adjust(left=0.07, bottom=0.1, right=0.54)
# меняем проценты на тексе из sizes
sizes = list(map(lambda x: str(x).replace('.', ','), sizes))
for i, a in enumerate(autotexts):
       a.set_text(f"{sizes[i]}00 ₽")

# вывод на дисплей
plt.show()