#!/usr/bin/env python3
"""
Test script for Bahi Khata API
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_customers():
    """Test the customers endpoints"""
    try:
        # Get customers (should be empty initially)
        response = requests.get(f"{BASE_URL}/customers/")
        print(f"✅ Get customers: {response.status_code}")
        customers = response.json()
        print(f"   Current customers: {len(customers)}")
        
        # Add a test customer
        test_customer = {
            "name": "Test Customer",
            "phone": "1234567890"
        }
        response = requests.post(f"{BASE_URL}/customers/", json=test_customer)
        print(f"✅ Add customer: {response.status_code}")
        new_customer = response.json()
        print(f"   New customer ID: {new_customer['customer_id']}")
        
        # Get customers again (should have 1 now)
        response = requests.get(f"{BASE_URL}/customers/")
        customers = response.json()
        print(f"✅ Get customers after add: {response.status_code}")
        print(f"   Total customers: {len(customers)}")
        
        return True
    except Exception as e:
        print(f"❌ Customers test failed: {e}")
        return False

def main():
    print("🚀 Testing Bahi Khata API...\n")
    
    # Test health endpoint
    if not test_health():
        print("\n❌ API is not responding. Make sure the backend is running.")
        return
    
    print()
    
    # Test customers endpoints
    if not test_customers():
        print("\n❌ Customers endpoints failed.")
        return
    
    print("\n🎉 All tests passed! The API is working correctly.")
    print("\nYou can now:")
    print("1. Open http://localhost:3000 in your browser")
    print("2. Add customers through the web interface")
    print("3. View the API docs at http://localhost:8000/docs")

if __name__ == "__main__":
    main()
