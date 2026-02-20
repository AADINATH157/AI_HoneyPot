#!/bin/bash

echo "========================================"
echo "AI Honeypot System - Startup Script"
echo "========================================"
echo ""

echo "[1/4] Checking dependencies..."
if ! pip show flask &> /dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "[2/4] Training ML model..."
if [ ! -f model.pkl ]; then
    python3 train_model.py
else
    echo "Model already exists. Skipping training."
fi

echo "[3/4] Starting Flask server on port 8000..."
python3 server.py &
SERVER_PID=$!

sleep 3

echo "[4/4] Starting Honeypot on port 9999..."
python3 honeypot.py &
HONEYPOT_PID=$!

echo ""
echo "========================================"
echo "System started successfully!"
echo "Web Dashboard: http://localhost:8000"
echo "Honeypot listening on port 9999"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop all services..."

trap "kill $SERVER_PID $HONEYPOT_PID 2>/dev/null; exit" INT TERM

wait
