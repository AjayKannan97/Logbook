# Logbook Backend API

A FastAPI-based backend service for the Logbook customer management system.

## Features

- **Customer Management**: Create, read, and manage customer records
- **Payment Status Tracking**: Track payment status (yet to pay, processing, paid)
- **Transaction Logging**: Record and track customer transactions
- **Audit Trail**: Comprehensive logging of all database changes
- **Search Functionality**: Search customers across all fields
- **RESTful API**: Clean, documented API endpoints

## Tech Stack

- **Framework**: FastAPI (Python 3.8+)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: None (development setup)
- **Documentation**: Auto-generated OpenAPI/Swagger docs

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup:**
   ```bash
   # Create PostgreSQL database
   CREATE DATABASE logbook;
   
   # Or use the provided schema file
   psql -d logbook -f logbook.sql
   ```

5. **Environment Variables (optional):**
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost:5432/logbook"
   ```

## Running the Server

```bash
# Activate virtual environment
source .venv/bin/activate

# Start the server
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Core Endpoints
- `GET /` - Health check
- `GET /customers/` - Get all customers
- `POST /customers/` - Create a new customer
- `GET /customers/search/?q={query}` - Search customers
- `POST /transactions/` - Add a new transaction

### API Documentation
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Database Schema

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

## Customer Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | ✅ | Customer's full name |
| phone | string | ❌ | Phone number |
| amount | numeric | ❌ | Amount/balance |
| status | string | ✅ | Payment status |
| upi_vpa | string | ❌ | UPI Virtual Payment Address |
| credit_limit | numeric | ❌ | Credit limit |
| billing_cycle_day | integer | ❌ | Day of month for billing |

## Status Values

- **"yet to pay"** - Payment pending
- **"processing"** - Payment being processed
- **"paid"** - Payment completed

## Development

### Project Structure
```
backend/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── logbook.sql         # Database schema
├── test_api.py         # API testing script
└── README.md           # This file
```

### Adding New Features
1. Update the SQLAlchemy models in `main.py`
2. Add new Pydantic schemas for request/response validation
3. Create new API endpoints
4. Update database schema if needed
5. Test with the provided test script

## Testing

Run the test script to verify API functionality:
```bash
python test_api.py
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check database credentials in DATABASE_URL
   - Verify database exists

2. **Port Already in Use**
   ```bash
   lsof -ti:8000 | xargs kill -9 2>/dev/null || echo "No process on port 8000"
   ```

3. **Import Errors**
   - Ensure virtual environment is activated
   - Check all dependencies are installed

4. **Database Schema Issues**
   - Run the migration script if needed
   - Check table structure matches models

### Logs
- Check console output for detailed error messages
- Database logs are stored in the `logs` table
- API access logs are displayed in the console

## Deployment

### Production Considerations
- Use environment variables for sensitive data
- Implement proper authentication/authorization
- Use production-grade database (not SQLite)
- Set up proper logging and monitoring
- Use HTTPS in production
- Consider using Gunicorn or uWSGI with FastAPI

## License

This project is open source and available under the MIT License.
