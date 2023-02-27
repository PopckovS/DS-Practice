import numpy as np

def f1():
    arr = np.arange(0, 11)
    print(arr)
    print('Получаем элемент по индексу arr[5] = ', arr[5])
    print('Получаем элементы от и до arr[1:5] = ', arr[:5])
    print('Получаем элементы от и до arr[5:8] = ', arr[5:])
    print('Получаем все элементы arr[:] = ', arr[:])


def f2():
    """broadcast"""
    arr = np.arange(0, 11)
    arr[:5] = 100
    print(arr)


def f3():
    """slice"""
    arr = np.arange(0, 11)
    print('Массив arr = ', arr)

    slice_arr = arr[:5]
    print('Срез slice_arr = ', slice_arr)
    slice_arr[:] = 100
    print('Срез после изменения slice_arr', slice_arr)
    print('Исходный массив после изменения среза', arr)

    arr = np.arange(0, 11)
    new_slice_arr = arr[:5].copy()
    print('Новый срез new_slice_arr = ', new_slice_arr)
    new_slice_arr[:] = 99
    print('Новый срез после из изменения new_slice_arr = ', new_slice_arr)
    print('Исходный массив arr = ', arr)


def f4():
    arr_m = np.array(
        [
            [5,  10, 15],
            [20, 25, 30],
            [35, 40, 45]
        ]
    )
    print(arr_m)
    print(arr_m.dtype)

    print('Получаем строки матрицы')
    print('Получаем 1-ю строку массива arr_m[0] = ', arr_m[0])
    print('Получаем 2-ю строку массива arr_m[1] = ', arr_m[1])

    print('Получаем элементы строк в матрице')
    print('Получаем 1-й элемент 1-й строки массива arr_m[1][0] = ', arr_m[1][0])
    print('Специальный синтаксис доступа arr_m[1,0] = ', arr_m[1,0])

    print('Получаем под-матрицу из матрицы')
    print('Получаем под-матрицу с помощью срезов arr_m[:2, 0:] = \n', arr_m[:2, 1:])


def f5():
    """Выбор по условию. Condition selection(filtering)"""
    arr = np.arange(1, 11)

    print(arr)

    new_arr = arr > 4
    print(new_arr)
    print(arr[new_arr])

    print(arr[arr > 4])


def f6():
    arr = np.arange(1,11)

    print('Простейшие операции с массивом: ', arr)
    print(arr+5)
    print(arr-5)
    print(arr*2)
    print(arr/2)



if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    # f4()
    # f5()
    f6()

