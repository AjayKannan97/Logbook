#!/bin/bash

# Logbook Startup Script
# This script starts both the backend and frontend services

echo "🚀 Starting Logbook Application..."
echo "=================================="

# Function to kill processes on specific ports
kill_port() {
    local port=$1
    local process_name=$2
    echo "🔄 Checking for existing $process_name process on port $port..."
    lsof -ti:$port | xargs kill -9 2>/dev/null && echo "✅ Killed existing $process_name process" || echo "ℹ️  No $process_name process found on port $port"
}

# Kill any existing processes
kill_port 8000 "Backend"
kill_port 3000 "Frontend"

echo ""
echo "🔧 Starting Backend Server..."
echo "-----------------------------"

# Start backend in background
cd backend
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

echo "🔌 Activating virtual environment..."
source .venv/bin/activate

echo "📥 Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

echo "🚀 Starting FastAPI server..."
python main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Check if backend is running
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✅ Backend server started successfully on http://localhost:8000"
else
    echo "❌ Failed to start backend server"
    exit 1
fi

echo ""
echo "🎨 Starting Frontend Server..."
echo "------------------------------"

# Start frontend in background
cd ../frontend

echo "📥 Installing dependencies..."
npm install > /dev/null 2>&1

echo "🚀 Starting React development server..."
npm run dev &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 5

# Check if frontend is running
if curl -s http://localhost:3000/ > /dev/null; then
    echo "✅ Frontend server started successfully on http://localhost:3000"
else
    echo "❌ Failed to start frontend server"
    exit 1
fi

echo ""
echo "🎉 Logbook Application is now running!"
echo "======================================"
echo "🌐 Frontend: http://localhost:3000"
echo "🔌 Backend API: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both services"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ All services stopped"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Keep script running
wait
