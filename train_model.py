print("Starting model training...")


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import random

def simulate_data():
    rows = []
    for _ in range(500):
        ip_len = random.randint(5, 15)
        data_len = random.randint(10, 1000)
        label = 1 if data_len > 500 else 0
        rows.append([ip_len, data_len, label])
    return pd.DataFrame(rows, columns=["ip_len", "data_len", "label"])

def train():
    df = simulate_data()
    X = df[["ip_len", "data_len"]]
    y = df["label"]

    clf = RandomForestClassifier()
    clf.fit(X, y)

    joblib.dump(clf, "model.pkl")
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train()
