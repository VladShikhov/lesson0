from time import sleep
print('Потыкаем палкой в numpy', '', '', sep='\n')
sleep(1.5)


# _numpy_
import numpy as np


print('Первое знакомство с numpy')
sleep(1)

# numpy _ инициализация массива
a = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
a[1, 1] = 0 # новый доступ, йоу
print('Инициализация массива numpy: ', a, sep='\n')
print()
sleep(1)

# numpy _ игры с массивом
b = a[0]
b[1] = 777
print('Небольшой эксперимент')
print('b:', b)
print('a:', a, sep='\n')
print('Итог: изменение исходного массива через изменеие нового')
print()
sleep(1)

# numpy _ атрибуты массива: ndim, shape, size, dtype
# посмотрим в каком измерении живет массив:
print(f'Измерение массива а: {a.ndim}', f'Измерение массива b: {b.ndim}', sep='\n')
print()
sleep(1)

# посмотрим на количество элементов в каждом измерении массива
count = 0
for i in a.shape:
    count += 1
    print(f'В измерени массива а номер {count} колличество элементов составляет {i}')
print()
sleep(1)

# посмотрим общее колличество элементов массивов
print(f'В массиве а: {a.size} элемента(-ов)', f'В массиве b: {b.size} элемента(-ов)', sep='\n')
print()
sleep(1)

# узнаем тип данных массива
c = np.array([['a', 'b'], ['c', 'd'], ['f', 'e']])
print(f'Тип данных массива а: {a.dtype}', f'Тип данных массива c: {c.dtype}', sep='\n')
print()
sleep(1)

# объединение массивов:
b = np.array([[0, 3, 4], [2, 7, 8]])
print('Объединение массивов:', np.concatenate((a, b), axis=0), sep='\n')
print()
sleep(1)

# вычисление колличества элементов по измерениям
abc = np.array([[[0, 0, 0],
                 [1, 1, 1]],
                [[0, 0, 0],
                 [2, 2, 2]],
                [[0, 0, 0],
                 [3, 3, 3]]])
print(f'Колличество осей (измерений) массива abc: {abc.ndim}', 
      f'Общее колличество элементов массива abc: {abc.size}', 
      f'Колличество элементов в каждом измерении: {abc.shape}', sep='\n')
print()
sleep(1)

# магия уравнений
predictions = np.array([[1, 2, 3, 4]])
labels = np.array([[5, 6, 7, 8]])
mse = (1 / 4) * np.sum(np.square(predictions - labels))
print('Mean Square Error(n=4): ', mse)