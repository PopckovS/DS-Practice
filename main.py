import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def func_1():
    # Выбор программы для отображения
    matplotlib.use('Qt5Agg')

    # Узнать что используется для отображения
    print('Для рисования используем = ', matplotlib.get_backend())

    # Передаем параметры для Y-оси
    plt.plot([1, 2, -6, 0, 4])

    # Показать график
    plt.show()





func_1()

