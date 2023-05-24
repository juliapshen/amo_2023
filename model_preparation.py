import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data_path = "train/"


def load_data(data_path):
    data = []
    for filename in os.listdir(data_path):
        if filename.endswith("_scaled.txt"):
            filepath = os.path.join(data_path, filename)
            df = pd.read_csv(filepath, header=None)
            data.append(df)
    return pd.concat(data, axis=0, ignore_index=True)


if __name__ == '__main__':
    data = load_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.1,
                                                        random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Сохранение обученной модели в файл
    joblib.dump(model, "trained_model.pkl")
