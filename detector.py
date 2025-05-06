import joblib

model = joblib.load("model.pkl")

def detect_malicious(ip, port, data):
    features = [[len(ip), len(data)]]
    pred = model.predict(features)
    return pred[0] == 1
