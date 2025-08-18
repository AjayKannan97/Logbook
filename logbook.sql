-- Customers Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    amount NUMERIC(10, 2),
    status TEXT NOT NULL DEFAULT 'yet to pay' CHECK (status IN ('yet to pay', 'processing', 'paid')),
    upi_vpa TEXT,
    credit_limit NUMERIC(10, 2),
    billing_cycle_day INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Transactions Table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
    type TEXT CHECK (type IN ('purchase', 'payment')),
    amount NUMERIC(10, 2) NOT NULL,
    description TEXT,
    date TIMESTAMP DEFAULT NOW()
);

-- Logs Table
CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY,
    table_name TEXT NOT NULL,
    action TEXT NOT NULL,
    record_id INT NOT NULL,
    old_data JSONB,
    new_data JSONB,
    timestamp TIMESTAMP DEFAULT NOW()
);
