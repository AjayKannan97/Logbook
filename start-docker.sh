#!/bin/bash

# Logbook Docker Startup Script
echo "🐳 Starting Logbook with Docker..."
echo "=================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker Desktop first."
    exit 1
fi

# Function to cleanup containers
cleanup() {
    echo ""
    echo "🛑 Stopping containers..."
    docker-compose down
    echo "✅ Containers stopped"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Build and start services
echo "🔨 Building and starting services..."
docker-compose up --build

echo ""
echo "🎉 Logbook is now running with Docker!"
echo "======================================"
echo "🌐 Frontend: http://localhost:3000 (run 'npm run dev' in frontend/ directory)"
echo "🔌 Backend API: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/docs"
echo "🗄️  Database: localhost:5432 (postgres/logbook)"
echo "🔧 pgAdmin: http://localhost:5050 (admin@logbook.com / admin123)"
echo ""
echo "Press Ctrl+C to stop all services"
