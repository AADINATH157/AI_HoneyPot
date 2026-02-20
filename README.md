# AI Honeypot System

A machine learning-powered honeypot system with real-time threat detection and web-based monitoring.

## Features
- Multi-threaded socket honeypot on port 9999
- ML-based malicious traffic detection
- Real-time web dashboard
- CSV logging with proper headers
- Cross-platform support (Windows/Linux/macOS)

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the ML Model
```bash
python train_model.py
```
This creates `model.pkl` with features: [ip_len, data_len]

### 3. Start the Backend Server (Port 8000)
```bash
python server.py
```

### 4. Start the Honeypot (Port 9999)
Open a new terminal:
```bash
python honeypot.py
```

### 5. Access Web Dashboard
Open browser: http://localhost:8000

## Testing

### Simulate Attack
```bash
python simulate_attack.py
```

### Manual Test
```bash
# Windows
echo "GET / HTTP/1.1" | nc localhost 9999

# Linux/macOS
echo "GET / HTTP/1.1" | nc localhost 9999
```

## Architecture

### Components
1. **honeypot.py** - Multi-threaded socket server (port 9999)
2. **detector.py** - ML-based threat detection
3. **logger.py** - CSV logging with headers
4. **server.py** - Flask backend (port 8000)
5. **index.html** - Web dashboard
6. **train_model.py** - ML model training

### Data Flow
```
Client → Honeypot (9999) → Detector → Logger → connections.csv
                                                      ↓
Browser → Server (8000) → connections.csv (display)
```

## File Formats

### connections.csv
```csv
timestamp,ip,port,data_length,is_malicious,attack_type
2025-01-15T10:30:00,127.0.0.1,12345,850,True,DDoS Attack
```

## Troubleshooting

### Port Already in Use
- Change PORT in honeypot.py or server.py
- Kill existing process: `netstat -ano | findstr :9999` (Windows)

### Model Not Found
- Run: `python train_model.py`

### CSV Not Loading
- Ensure server.py is running
- Check browser console for errors

## Security Notes
- Run honeypot in isolated environment
- Monitor connections.csv for suspicious activity
- Adjust detection threshold in detector.py as needed

## Cross-Platform Compatibility
- Uses os.path.join() for file paths
- Socket timeout prevents hanging connections
- Threading for concurrent connections
- Graceful shutdown with Ctrl+C
