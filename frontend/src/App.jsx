import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

export default function App() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [amount, setAmount] = useState("");
  const [status, setStatus] = useState("yet to pay");
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchCustomers();
  }, []);

  const fetchCustomers = async () => {
    try {
      const res = await axios.get("http://localhost:8000/customers/");
      setCustomers(res.data);
    } catch (error) {
      console.error("Error fetching customers:", error);
    }
  };

  const searchCustomers = async (query) => {
    try {
      const res = await axios.get(`http://localhost:8000/customers/search/?q=${encodeURIComponent(query)}`);
      setCustomers(res.data);
    } catch (error) {
      console.error("Error searching customers:", error);
    }
  };

  const addCustomer = async () => {
    if (!name.trim()) return;
    
    // Validate amount if provided
    if (amount.trim() && isNaN(parseFloat(amount.trim()))) {
      alert("Please enter a valid amount");
      return;
    }
    
    setLoading(true);
    try {
      await axios.post("http://localhost:8000/customers/", {
        name: name.trim(),
        phone: phone.trim() || null,
        amount: amount.trim() ? parseFloat(amount.trim()) : null,
        status: status
      });
      setName("");
      setPhone("");
      setAmount("");
      setStatus("yet to pay");
      await fetchCustomers();
    } catch (error) {
      console.error("Error adding customer:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addCustomer();
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1 className="title">Logbook</h1>
        <p className="subtitle">Customer Management System</p>
        
        <div className="input-section">
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Customer name"
            className="input-field"
            disabled={loading}
          />
          <input
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Phone number (optional)"
            className="input-field"
            disabled={loading}
          />
          <input
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Amount (optional)"
            className="input-field"
            disabled={loading}
          />
          <select
            value={status}
            onChange={(e) => setStatus(e.target.value)}
            className="input-field"
            disabled={loading}
          >
            <option value="yet to pay">Yet to Pay</option>
            <option value="processing">Processing</option>
            <option value="paid">Paid</option>
          </select>
          <button 
            onClick={addCustomer} 
            className="add-button"
            disabled={loading || !name.trim()}
          >
            {loading ? "Adding..." : "Add Customer"}
          </button>
        </div>

        <div className="search-section">
          <input
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && searchCustomers(searchQuery)}
            placeholder="Search customers by name, phone, status, or amount..."
            className="search-field"
          />
          <button 
            onClick={() => searchCustomers(searchQuery)}
            className="search-button"
          >
            Search
          </button>
          <button 
            onClick={() => {
              setSearchQuery("");
              fetchCustomers();
            }}
            className="clear-button"
          >
            Clear
          </button>
        </div>

        <div className="customers-section">
          <h2 className="section-title">Customers ({customers.length})</h2>
          {customers.length === 0 ? (
            <p className="no-customers">No customers yet. Add your first customer above!</p>
          ) : (
            <ul className="customers-list">
              {customers.map((customer) => (
                <li key={customer.customer_id} className="customer-item">
                  <span className="customer-name">{customer.name}</span>
                  {customer.phone && (
                    <span className="customer-phone">{customer.phone}</span>
                  )}
                  {customer.amount && (
                    <span className="customer-amount">₹{customer.amount}</span>
                  )}
                  <span className={`customer-status status-${customer.status.replace(/\s+/g, '-')}`}>
                    {customer.status}
                  </span>
                  <span className="customer-date">
                    {new Date(customer.created_at).toLocaleDateString()}
                  </span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
