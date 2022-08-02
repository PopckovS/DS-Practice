import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import pandas as pd
import math

import seaborn as sns

import statistics


def func0():

    # сами значения
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # частота появления значений
    y = [1, 2, 4, 7, 9, 7, 4, 2, 1]

    plt.plot(x, y)

    plt.grid()
    plt.show()


def func1():
    mass = [161, 164, 157, 166, 167, 167, 159, 165, 166, 167]
    ca = 163.9
    result = 0

    for elem in mass:
        result += int(ca - elem)
        print('- ', int(ca - elem))

    print('result = ', result)
    print('mass = ', np.mean(mass))

    # plt.plot(y)
    #
    # plt.grid()
    # plt.show()


def func2():
    values = [1, 2, 3, 4, 5]
    keys = ['a', 'b', 'c', 'd', 'e']
    s1 = pd.Series(values, keys)

    print(s1)

    print('a = ', s1['a'])
    print('c = ',s1['c'])


def func3():
    query = """
    SELECT 'id', 'stadiya_vypolneniya', 'tip_zu',
    'nomer_na_sheme', 'kad_num_sushchestvuyushchego_zu'
    FROM gis_data.proektnye_uchastki
    WHERE kad_num_obraz_zu='69:10:0000026:1442';
    """
    connect_param = {
        "host": "localhost",
        "database": "work_ngw",
        "user": "ngw_admin",
        "password": "123"
    }
    connect = psycopg2.connect(**connect_param)

    df = pd.read_sql(query, con=connect)
    df.to_dict(orient='records')
    print(df)


def func4():
    # набор наблюдений, их среднее, и количество наблюдений всего
    array = [161, 164, 157, 166, 167, 167, 159, 165, 166, 167]
    mean, count = np.mean(array), len(array)
    dispersion, tmp = None, 0

    tmp = [(elem - mean)**2 for elem in array]
    dispersion = sum(tmp)/count

    print('Дисперсия с помощью numpy = ', np.var(array))
    print('Дисперсия своим счетом = ', dispersion)
    print('Среднеквадратическое отклонение взятое от Дисперсии = ', math.sqrt(dispersion))


def func5():

    array = [
        185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166,
        167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171
    ]

    result = np.array_split(array, 4)

    print('result = ', result)

    # Вывод
    #  result =
    #  [array([185, 175, 170, 169, 171, 172, 175, 157]),
    #  array([170, 172, 167, 173, 168, 167, 166, 167]),
    #  array([169, 172, 177, 178, 165, 161, 179]),
    #  array([159, 164, 178, 172, 170, 173, 171])]


def func6():

    array = [
        185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166,
        167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171
    ]

    plt.boxplot(array)

    plt.grid()
    plt.show()


def func7():
    path = 'Путь к файлу'
    sheet_name = 'название страницы'

    # получаем записи в виде словарей, {столбец:ячейка} из указанной страницы
    df = pd.read_excel(path, na_filter=False, sheet_name=sheet_name)
    df = df.to_dict(orient='index')
    data = [elem for elem in df.values()]


def func8():
    x = [
        185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166,
        167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171
    ]

    values, counts = np.unique(x, return_counts=True)

    print('Все значения = ', values)
    print('Количество раз что они встречаются = ', counts)

    index = np.argmax(counts)

    print('Самое часто встречающееся число = ', values[index])
    print(f'Число {values[index]} встречается {counts[index]} раз')

    plt.plot(x)

    plt.grid()
    plt.show()


# func0()
# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
func8()






