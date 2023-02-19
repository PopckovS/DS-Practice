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
            [],
            [],
            []
        ]
    )


if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    f4()

