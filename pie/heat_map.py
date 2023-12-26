import numpy as np
import matplotlib.pyplot as plt

# Установка случайныъ данных
data = np.random.random((12, 12))
# отображения данных
plt.imshow(data)
# Установка заголовка
plt.title("Heat Map 2D")
plt.show()