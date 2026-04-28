#!/bin/bash

# Run all tests
echo "Running backend tests..."
cd backend
pytest tests/ -v --cov=app --cov-report=term

echo ""
echo "Running frontend tests..."
cd frontend
npm run test -- --run

echo ""
echo "All tests completed!"