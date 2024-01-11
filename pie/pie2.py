"""Создание аналогичного изобржения с помощью
инструментов  библиотеки matplotlib"""

#  импортируем зависимости
import matplotlib.pyplot as plt

# Указываем данные для переменных
sizes = [554.6, 822.6]
labels = ['Чистый прирост\n стоимости', 'Дивидетды (с\n учетом налогов']
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
ax.pie(sizes, colors=colors,
       autopct='%.2f%%', pctdistance=.4,
       startangle=90,
       radius=0.9,
       rotatelabels=True, labeldistance=0.95,
       wedgeprops=wedgeprops,
       textprops=textprops)
# устанавливаем даные для legend
fig.legend(labels=labels, bbox_to_anchor=(1.0, 0.7), labelcolor='white',
           fontsize=18, labelspacing = 4, frameon=False)
# вывод на дисплей
plt.show()