#!/bin/bash

# Build frontend for production
echo "Building frontend..."
cd frontend
npm install
npm run build

echo ""
echo "Building backend..."
cd backend
pip install -r requirements.txt

echo ""
echo "Build complete!"
echo "Frontend dist: frontend/dist/"
echo "Backend ready to run with: uvicorn app.main:app"