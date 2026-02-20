from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from logger import log_connection
from detector import detect_malicious

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/log_connection', methods=['POST'])
def log_connection_endpoint():
    try:
        data = request.get_json()
        ip = data.get('ip', 'unknown')
        port = data.get('port', 0)
        data_length = data.get('dataLength', 0)
        
        simulated_data = 'x' * data_length
        is_malicious, attack_type = detect_malicious(ip, port, simulated_data)
        
        log_connection(ip, port, simulated_data, is_malicious, attack_type)
        
        return jsonify({'status': 'success', 'is_malicious': is_malicious, 'attack_type': attack_type}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/connections.csv')
def get_csv():
    try:
        return send_from_directory(BASE_DIR, 'connections.csv')
    except FileNotFoundError:
        return "connections.csv not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
