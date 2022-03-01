import numpy as np

mass = [
    185,175,170,169,171,172,175,157,170,172,167,173,168,167,166,
    167,169,172,177,178,165,161,179,159,164,178,172,170,173,171
]

values, counts = np.unique(mass, return_counts=True)

print('Все значения = ', values)
print('Количество раз что они встречаются = ', counts)

index = np.argmax(counts)

print('Самое часто встречающееся число = ', values[index])
print(f'Число {values[index]} встречается {counts[index]} раз')





