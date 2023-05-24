from sklearn.preprocessing import StandardScaler
import numpy as np
import os

def data_preprocessing(path):
    for folder_name in ['train', 'test']:
        folder_path = os.path.join(path, folder_name)
        file_names = os.listdir(folder_path)
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            data = np.loadtxt(file_path, delimiter=',', dtype=None)
            X = data[:, :-1] # выбираем все столбцы, кроме последнего
            y = data[:, -1] # выбираем последний столбец
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            data_scaled = np.hstack((X_scaled, y.reshape(-1, 1))) # объединяем масштабированные данные и целевую переменную
            new_file_path = os.path.join(folder_path, file_name[:-4] + '_scaled.txt')
            np.savetxt(new_file_path, data_scaled, delimiter=',')

if __name__ == '__main__':
    path = '.'
    data_preprocessing(path)