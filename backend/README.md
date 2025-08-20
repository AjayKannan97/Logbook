# Logbook Backend API

A FastAPI-based backend service for the Logbook customer management system, now with full Docker support and enhanced error handling.

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# From project root
./start-docker.sh

# Or manually
docker compose up --build
```

### Option 2: Local Development
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python main.py
```

## ✨ Features

- **Customer Management**: Create, read, and manage customer records
- **Payment Status Tracking**: Track payment status (yet to pay, processing, paid)
- **Transaction Logging**: Record and track customer transactions
- **Audit Trail**: Comprehensive logging of all database changes
- **Search Functionality**: Search customers across all fields
- **RESTful API**: Clean, documented API endpoints
- **Docker Support**: Full containerization with auto-reload
- **Enhanced Validation**: Improved error handling and debug logging
- **Real-time Logging**: Detailed request/response logging

## 🐳 Docker Support

### Development Container
```bash
# Build and run
docker compose up --build

# View logs
docker compose logs -f backend

# Restart after code changes
docker compose restart backend
```

### Production Container
```bash
# Use production Dockerfile
docker compose -f ../docker-compose.prod.yml up --build
```

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python 3.8+)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Validation**: Pydantic v2 with enhanced error handling
- **Containerization**: Docker with multi-stage builds
- **Documentation**: Auto-generated OpenAPI/Swagger docs
- **Logging**: Comprehensive debug and audit logging

## 📡 API Endpoints

### Core Endpoints
- `GET /` - Health check
- `GET /customers/` - Get all customers
- `POST /customers/` - Create a new customer
- `GET /customers/search/?q={query}` - Search customers
- `POST /transactions/` - Add a new transaction

### Testing & Debug
- `POST /test-customer/` - Test customer validation schema

### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

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

### Example Request
```json
{
  "name": "John Doe",
  "phone": "1234567890",
  "amount": 150.75,
  "status": "yet to pay",
  "credit_limit": 500.00
}
```

## 🔧 Enhanced Error Handling

### Validation Errors (422)
The API now provides detailed validation errors with debug logging:

```bash
# Check backend logs for detailed error information
docker compose logs backend

# Test validation endpoint
curl -X POST http://localhost:8000/test-customer/
```

### Debug Logging
- **Request Data**: Logs all received customer data
- **Validation Results**: Shows successful/failed validations
- **Database Operations**: Tracks all database changes
- **Error Details**: Comprehensive error information

## 🗄️ Database Schema

### Customers Table
```sql
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    amount NUMERIC(10, 2),
    status TEXT NOT NULL DEFAULT 'yet to pay' 
        CHECK (status IN ('yet to pay', 'processing', 'paid')),
    upi_vpa TEXT,
    credit_limit NUMERIC(10, 2),
    billing_cycle_day INT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Transactions Table
```sql
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
    type TEXT CHECK (type IN ('purchase', 'payment')),
    amount NUMERIC(10, 2) NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT NOW()
);
```

### Logs Table
```sql
CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY,
    table_name TEXT NOT NULL,
    action TEXT NOT NULL,
    record_id INT NOT NULL,
    old_data JSONB,
    new_data JSONB,
    timestamp TIMESTAMP DEFAULT NOW()
);
```

## 🚨 Troubleshooting

### Common Issues

1. **422 Unprocessable Entity**
   - Check required fields (name is mandatory)
   - Verify data types (amount should be numeric)
   - Ensure status is one of: "yet to pay", "processing", "paid"
   - View detailed logs: `docker compose logs backend`

2. **Docker Issues**
   ```bash
   # Start Docker Desktop
   open /Applications/Docker.app
   
   # Restart containers
   docker compose down
   ./start-docker.sh
   ```

3. **Database Connection Error**
   - Ensure PostgreSQL container is running
   - Check logs: `docker compose logs postgres`

4. **Code Changes Not Reflecting**
   ```bash
   # Restart backend container
   docker compose restart backend
   ```

### Viewing Logs
```bash
# All services
docker compose logs -f

# Backend only
docker compose logs -f backend

# Last N lines
docker compose logs --tail=50 backend
```

## 🔄 Development Workflow

### Making Changes
1. **Edit code** in your local directory
2. **Restart backend** to apply changes:
   ```bash
   docker compose restart backend
   ```
3. **Check logs** for any errors:
   ```bash
   docker compose logs backend
   ```

### Testing Changes
```bash
# Test customer creation
curl -X POST http://localhost:8000/customers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Customer", "amount": 100.50}'

# Test validation endpoint
curl -X POST http://localhost:8000/test-customer/
```

## 📝 Recent Updates

- ✅ **Docker Integration**: Full containerization with auto-reload
- ✅ **Enhanced Validation**: Improved Pydantic models and error handling
- ✅ **Debug Logging**: Comprehensive request/response logging
- ✅ **Test Endpoints**: Added validation testing endpoints
- ✅ **Better Error Messages**: Detailed 422 error information
- ✅ **Pydantic Compatibility**: Support for both v1 and v2 methods

## 📄 License

This project is open source and available under the MIT License.
