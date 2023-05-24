import os

import numpy as np

# Если папки "train" и "test" не созданы, то создаем их
if not os.path.exists('train'):
    os.mkdir('train')
if not os.path.exists('test'):
    os.mkdir('test')


# Функция для генерации набора данных температуры с аномалиями и шумами
def _generate_data():
    data = []
    days = 365
    anomaly = 5
    for i in range(days):
        temp = np.random.randint(0, 20)
        temp += np.random.uniform(-10, 10)
        if i <= anomaly:
            temp += 10 * anomaly
        data.append([i + 1, round(temp, 2)])
    return data


# Функция создания наборов данных
# quantity - число наборов
# name - имя файлов
def _create_data(name, number):
    for i in range(number):
        data = _generate_data()
        with open(name + f'{i}.txt', 'w') as file:
            file.writelines(str(d[0]) + ',' + str(d[1]) + '\n' for d in data)


if __name__ == '__main__':
    _create_data('train/data', 7)
    _create_data('test/data', 3)
