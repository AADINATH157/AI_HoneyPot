import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
clf = None

def load_model():
    global clf
    if clf is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"[!] Model file '{MODEL_PATH}' not found. Please train the model first.")
        with open(MODEL_PATH, "rb") as f:
            clf = pickle.load(f)

def detect_malicious(ip, port, data):
    load_model()
    ip_len = len(ip)
    data_len = len(data) if data else 0
    features = [[ip_len, data_len]]
    prediction = clf.predict(features)
    
    is_malicious = prediction[0] == 1
    attack_type = ""
    if is_malicious:
        if data_len > 800:
            attack_type = "DDoS Attack"
        elif "SELECT" in data.upper() or "DROP" in data.upper():
            attack_type = "SQL Injection"
        elif "<script>" in data.lower():
            attack_type = "XSS Attempt"
        else:
            attack_type = "Suspicious Activity"
    
    return is_malicious, attack_type