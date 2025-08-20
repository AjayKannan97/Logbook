# Logbook - Customer Management System

Logbook is a modern customer management system designed to help businesses efficiently manage and track their customer information. It's built as a full-stack web application with a FastAPI backend and React frontend, now fully containerized with Docker for easy deployment and development.

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Start everything with one command
./start-docker.sh

# Access your application:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Development
```bash
# Start backend and frontend locally
./start.sh
```

## ✨ Key Features

- **Customer Management**: Add, view, and manage customer details
- **Payment Tracking**: Track payment status (yet to pay, processing, paid)
- **Search Functionality**: Search across all customer fields
- **Transaction Logging**: Automatic audit trail for all changes
- **Responsive UI**: Modern React frontend with Vite
- **Docker Support**: Full containerization for easy deployment
- **Real-time Updates**: Hot-reload for development

## 🐳 Docker Setup (Recommended)

### Prerequisites
- Docker Desktop installed and running
- Git (to clone the repository)

### Quick Start with Docker
1. **Clone and navigate to the project:**
   ```bash
   git clone <your-repo-url>
   cd Logbook
   ```

2. **Start everything:**
   ```bash
   ./start-docker.sh
   ```

3. **Access your application:**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **Database**: PostgreSQL on localhost:5432
   - **pgAdmin**: http://localhost:5050 (admin@logbook.com / admin123)

### Docker Services
- **Frontend**: React development server with hot-reload
- **Backend**: FastAPI with auto-reload and debug logging
- **Database**: PostgreSQL 15 with persistent storage
- **pgAdmin**: Database management interface

### Docker Commands
```bash
# View running containers
docker compose ps

# View logs
docker compose logs -f

# Stop services
docker compose down

# Restart backend (after code changes)
docker compose restart backend
```

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL database

### Backend Setup
1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up database:**
   ```bash
   # Create PostgreSQL database
   createdb logbook
   
   # Or use the provided schema
   psql -d logbook -f backend/logbook.sql
   ```

4. **Run backend:**
   ```bash
   python backend/main.py
   ```

### Frontend Setup
1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

## 📡 API Endpoints

### Customer Management
- `GET /customers/` - Get all customers
- `GET /customers/search/?q={query}` - Search customers
- `POST /customers/` - Create new customer
- `GET /` - Health check

### Transaction Management
- `POST /transactions/` - Add new transaction
- `GET /transactions/` - Get all transactions

### Testing & Debug
- `POST /test-customer/` - Test customer validation

## 📊 Customer Data Model

### Required Fields
- **name** (string): Customer's full name

### Optional Fields
- **phone** (string): Contact phone number
- **amount** (float): Outstanding balance
- **status** (string): Payment status - "yet to pay", "processing", or "paid"
- **upi_vpa** (string): UPI Virtual Payment Address
- **credit_limit** (float): Customer's credit limit
- **billing_cycle_day** (integer): Day of month for billing cycle

### Example Customer Creation
```json
{
  "name": "John Doe",
  "phone": "1234567890",
  "amount": 150.75,
  "status": "yet to pay",
  "credit_limit": 500.00
}
```

## 🔧 Startup Scripts

### `start-docker.sh` (Recommended)
- Starts all services in Docker containers
- Automatically detects Docker Compose version
- Includes frontend, backend, and database
- **Usage**: `./start-docker.sh`

### `start.sh` (Local Development)
- Runs backend and frontend locally
- Uses local virtual environment
- **Usage**: `./start.sh`

## 🏗️ Project Structure

```
Logbook/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main API server
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Development container
│   └── Dockerfile.prod     # Production container
├── frontend/               # React frontend
│   ├── src/                # React components
│   ├── package.json        # Node.js dependencies
│   ├── Dockerfile          # Frontend container
│   └── vite.config.js      # Vite configuration
├── docker-compose.yml      # Development services
├── docker-compose.prod.yml # Production services
├── start-docker.sh         # Docker startup script
├── start.sh                # Local startup script
└── README.md               # This file
```

## 🚨 Troubleshooting

### Docker Issues
1. **"Docker daemon not running"**
   ```bash
   open /Applications/Docker.app  # Start Docker Desktop
   ```

2. **Port conflicts**
   ```bash
   docker compose down  # Stop containers
   ./start-docker.sh    # Restart
   ```

3. **Container not updating after code changes**
   ```bash
   docker compose restart backend  # Restart backend
   ```

### API Issues
1. **422 Unprocessable Entity**
   - Check required fields (name is mandatory)
   - Verify data types (amount should be numeric)
   - Ensure status is one of: "yet to pay", "processing", "paid"

2. **Database connection errors**
   - Ensure PostgreSQL container is running
   - Check logs: `docker compose logs postgres`

### Viewing Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f frontend

# Last N lines
docker compose logs --tail=50 backend
```

## 🚀 Production Deployment

### Production Docker
```bash
# Use production-optimized containers
docker compose -f docker-compose.prod.yml up --build
```

### Environment Variables
```bash
# Database configuration
DATABASE_URL=postgresql://user:password@host:5432/database

# Backend settings
PYTHONPATH=/app
```

## 📝 Recent Updates

- ✅ **Docker Integration**: Full containerization with frontend and backend
- ✅ **Frontend Service**: React app now runs in Docker container
- ✅ **Improved Scripts**: Automatic Docker Compose version detection
- ✅ **API Validation**: Enhanced error handling and debug logging
- ✅ **Startup Scripts**: One-command startup for both Docker and local modes
- ✅ **Better Logging**: Detailed debug information for troubleshooting

## 📄 License

This project is open source and available under the MIT License.
