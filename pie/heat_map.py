import numpy as np
import matplotlib.pyplot as plt

# Установка случайныъ данных
data = np.random.random((12, 12))
# Изменение цветовой карты
plt.imshow(data, cmap='autumn', interpolation='nearest')
# Установка заголовка
plt.title("Heat Map 2D")
# удаление осей x, y
plt.axis("off")
plt.show()