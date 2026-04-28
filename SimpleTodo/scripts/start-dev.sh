#!/bin/bash

# Start backend server
echo "Starting backend server..."
cd backend
pip install -r requirements.txt -q
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

# Start frontend server
echo "Starting frontend server..."
cd frontend
npm install -q
npm run dev &

echo "Both servers started!"
echo "Frontend: http://localhost:3000"
echo "Backend: http://localhost:8000"
echo "Press Ctrl+C to stop both servers"

wait