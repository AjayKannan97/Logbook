# Logbook - Customer Management System

A modern customer management system built with FastAPI (Python) backend and React frontend.

## Features

- Add and manage customers with name, phone, amount, and payment status
- Track customer information (name, phone, amount, status, credit limit, etc.)
- Search functionality across all customer fields
- Payment status tracking (yet to pay, processing, paid)
- Transaction logging
- Audit trail for all changes
- Modern, responsive UI

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL database

## Setup Instructions

### 1. Database Setup

First, create a PostgreSQL database:

```sql
CREATE DATABASE logbook;
```

You can use the provided `logbook.sql` file to create the tables, or the application will create them automatically.

### 2. Backend Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (optional):
```bash
export DATABASE_URL="postgresql://username:password@localhost:5432/logbook"
```

4. Run the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 3. Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `GET /` - Health check
- `GET /customers/` - Get all customers
- `GET /customers/search/?q={query}` - Search customers across all fields
- `POST /customers/` - Create a new customer
- `POST /transactions/` - Add a new transaction

## Customer Fields

The customer creation endpoint accepts the following fields:

- **name** (required): Customer's full name
- **phone** (optional): Customer's phone number
- **amount** (optional): Customer's amount/balance (numeric value)
- **status** (required): Payment status - "yet to pay", "processing", or "paid"
- **upi_vpa** (optional): UPI Virtual Payment Address
- **credit_limit** (optional): Customer's credit limit
- **billing_cycle_day** (optional): Day of month for billing cycle

## Project Structure

```
├── main.py              # FastAPI backend server
├── requirements.txt     # Python dependencies
├── package.json         # Node.js dependencies
├── vite.config.js       # Vite configuration
├── index.html           # Main HTML file
├── src/
│   ├── main.jsx        # React entry point
│   ├── App.jsx         # Main React component
│   └── App.css         # Styling
└── logbook.sql         # Database schema
```

## Development

- Backend: FastAPI with SQLAlchemy ORM
- Frontend: React with Vite
- Database: PostgreSQL
- Styling: Custom CSS with modern design

## Troubleshooting

1. **Database Connection Error**: Make sure PostgreSQL is running and the database exists
2. **Port Already in Use**: Change ports in `main.py` (backend) or `vite.config.js` (frontend)
3. **CORS Issues**: The backend is configured to allow requests from localhost:3000 and localhost:5173

### Port Conflicts

If you encounter "port already in use" errors, you can kill processes using these ports:

**Kill process on port 8000 (Backend):**
```bash
lsof -ti:8000 | xargs kill -9 2>/dev/null || echo "No process on port 8000"
```

**Kill process on port 3000 (Frontend):**
```bash
lsof -ti:3000 | xargs kill -9 2>/dev/null || echo "No process on port 3000"
```

These commands will forcefully terminate any processes running on the specified ports, allowing you to restart your servers.

### Database Migration

If you're upgrading from an older version and need to add the amount and status fields to existing customers table:

```bash
# The application will automatically create the amount and status columns
# If you need to manually add them:
ALTER TABLE customers ADD COLUMN amount NUMERIC(10, 2);
ALTER TABLE customers ADD COLUMN status TEXT NOT NULL DEFAULT 'yet to pay' CHECK (status IN ('yet to pay', 'processing', 'paid'));
```

## License

This project is open source and available under the MIT License.
