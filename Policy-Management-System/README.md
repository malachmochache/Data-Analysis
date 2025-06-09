# 🛡️ Policy Management System

This is a simple Python-based insurance policy management system for an insurance company. It includes policyholders, products, and payments with basic functionality and error handling. The system allows policy managers to perform various tasks, such as adding and suspending policyholders, registering new members, and managing policy products. 

---

## 📁 Project Structure

```
policy-management-system/
│
├── policyholder.py               # Class for policyholder management
├── product.py                    # Class for product management
├── payment.py                    # Class for payment processing
├── main.py                       # Demo and testing script
├── README.md                     # Instructions and documentation
└── policy-management-system.zip  # ZIP file for assignment submission
```

---

## ✅ Features

### 🧑‍💼 Policyholder Management
- Register new policyholders
- Suspend/reactivate accounts
- Assign products and record payments

### 📦 Product Management
- Create new insurance products
- Update product name and price
- Suspend/remove products

### 💳 Payment Management
- Record and process payments
- Check for overdue payments
- Generate payment reminders and penalties

### 🛑 Exception Handling
- Handles invalid inputs
- Prevents duplicate registrations
- Catches errors in payment processing or product assignment

---

## 💻 How to Run the Project

1. **Clone or Download** the repository or unzip the "prolicy-management-system" file:
   ```bash
   git clone https://github.com/your-username/policy-management-system.git
   cd policy-management-system
   ```

2. **Run the main script**:
   ```bash
   python main.py
   ```

3. Output will display sample policyholder info and payment processing status.

---

## 🔒 Example Output

```
=== Policyholder Accounts ===
ID: 1, Name: John Doe, Email: john@example.com, Status: Active, Products: ['Life Insurance'], Payments: [1000]
ID: 2, Name: Jane Smith, Email: jane@example.com, Status: Active, Products: ['Health Insurance'], Payments: [1500]

=== Payment Info ===
Amount: 1000, Status: Paid, Due Date: 2025-06-04 Penalty: 50.0
Amount: 1500, Status: Paid, Due Date: 2025-06-14 Penalty: 0.0
```

---

## 🔧 Requirements

This project only uses Python standard libraries, so **no external packages** are required. To ensure compatibility, use:

- Python 3.8 or newer

---

## 👨‍🎓 Author

Malach Mochache | Nexford University