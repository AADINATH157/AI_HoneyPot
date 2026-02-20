import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import random
import os

def simulate_data():
    rows = []
    for _ in range(500):
        ip_len = random.randint(7, 15)
        data_len = random.randint(10, 1000)
        label = 1 if data_len > 500 else 0
        rows.append([ip_len, data_len, label])
    return pd.DataFrame(rows, columns=["ip_len", "data_len", "label"])

def train():
    df = simulate_data()
    X = df[["ip_len", "data_len"]]
    y = df["label"]

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)

    model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    joblib.dump(clf, model_path)
    print(f"Model trained and saved as {model_path}")
    print(f"Model expects features: [ip_len, data_len]")
    print(f"Training accuracy: {clf.score(X, y):.2f}")

if __name__ == "__main__":
    train()