from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import json
import os

# Database configuration - using environment variables or defaults
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://wingman2.0@localhost:5432/logbook")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    amount = Column(Numeric(10, 2))
    status = Column(String, nullable=False, default="yet to pay")
    upi_vpa = Column(String)
    credit_limit = Column(Numeric(10, 2))
    billing_cycle_day = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    type = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(Text)
    date = Column(TIMESTAMP, default=datetime.utcnow)

class Log(Base):
    __tablename__ = "logs"
    log_id = Column(Integer, primary_key=True, index=True)
    table_name = Column(String)
    action = Column(String)
    record_id = Column(Integer)
    old_data = Column(Text)
    new_data = Column(Text)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Logbook API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class CustomerCreate(BaseModel):
    name: str
    phone: str = None
    amount: float = None
    status: str = "yet to pay"
    upi_vpa: str = None
    credit_limit: float = None
    billing_cycle_day: int = None
    
    @validator('status')
    def validate_status(cls, v):
        valid_statuses = ["yet to pay", "processing", "paid"]
        if v not in valid_statuses:
            raise ValueError(f"Status must be one of: {valid_statuses}")
        return v
    
    def to_dict(self):
        """Convert to dict for compatibility"""
        try:
            return self.model_dump()
        except AttributeError:
            return self.dict()

class TransactionCreate(BaseModel):
    customer_id: int
    type: str
    amount: float
    description: str = None
    
    def to_dict(self):
        """Convert to dict for compatibility"""
        try:
            return self.model_dump()
        except AttributeError:
            return self.dict()

# Helper - log changes
def log_action(session, table, action, record_id, old_data, new_data):
    log_entry = Log(
        table_name=table,
        action=action,
        record_id=record_id,
        old_data=json.dumps(old_data) if old_data else None,
        new_data=json.dumps(new_data) if new_data else None
    )
    session.add(log_entry)

# Routes
@app.post("/customers/")
def create_customer(customer: CustomerCreate):
    print(f"Received customer data: {customer.to_dict()}")  # Debug logging
    db = SessionLocal()
    try:
        new_customer = Customer(**customer.to_dict())
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        log_action(db, "customers", "INSERT", new_customer.customer_id, None, customer.to_dict())
        print(f"Customer created successfully with ID: {new_customer.customer_id}")  # Debug logging
        return new_customer
    except Exception as e:
        db.rollback()
        print(f"Error creating customer: {e}")  # Debug logging
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/customers/")
def get_customers():
    db = SessionLocal()
    try:
        return db.query(Customer).all()
    finally:
        db.close()

@app.get("/customers/search/")
def search_customers(q: str = ""):
    db = SessionLocal()
    try:
        if not q:
            return db.query(Customer).all()
        
        # Search across multiple fields
        search_query = f"%{q}%"
        customers = db.query(Customer).filter(
            (Customer.name.ilike(search_query)) |
            (Customer.phone.ilike(search_query)) |
            (Customer.status.ilike(search_query)) |
            (Customer.amount.cast(String).ilike(search_query))
        ).all()
        return customers
    finally:
        db.close()

@app.post("/transactions/")
def add_transaction(txn: TransactionCreate):
    db = SessionLocal()
    try:
        new_txn = Transaction(**txn.to_dict())
        db.add(new_txn)
        db.commit()
        db.refresh(new_txn)
        log_action(db, "transactions", "INSERT", new_txn.transaction_id, None, txn.to_dict())
        return new_txn
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Logbook API is running!"}

@app.post("/test-customer/")
def test_customer_creation():
    """Test endpoint to debug customer creation"""
    test_data = {
        "name": "Test Customer",
        "phone": "1234567890",
        "amount": 100.50,
        "status": "yet to pay"
    }
    
    try:
        customer = CustomerCreate(**test_data)
        return {
            "message": "CustomerCreate validation successful",
            "data": customer.to_dict(),
            "validation": "passed"
        }
    except Exception as e:
        return {
            "message": "CustomerCreate validation failed",
            "error": str(e),
            "data": test_data,
            "validation": "failed"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

