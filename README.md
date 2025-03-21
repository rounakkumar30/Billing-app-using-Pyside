
# PySide6 Billing System  

## 📌 Project Overview  
This is a **desktop billing application** built using **PySide6 (Python GUI)** and **MySQL**. It allows users to:  
- Add customer details and create bills.  
- Store bills and customer data in a MySQL database.  
- Retrieve and display stored bills and customer information.  

---

## 🛠️ Technologies Used  
- **Python 3.9+**  
- **PySide6** (for GUI development)  
- **MySQL** (as the database)  
- **PyMySQL** (for database connectivity)  

---

## 🚀 Installation Guide  

### **1️⃣ Install Dependencies**  
Ensure Python is installed, then run:  

```sh
pip install PySide6 pymysql
```

---

### **2️⃣ Setup MySQL Database**  

#### **Create Database and Tables**  
Run the following SQL script in MySQL Workbench or phpMyAdmin:  

```sql
CREATE DATABASE billing_system;

USE billing_system;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_details TEXT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
```

---

## 📂 Project Structure  

```
billing_system/
│── billing_app.py      # Main GUI Application
│── db.py               # Database Connection Handler
│── README.md           # Documentation
└── requirements.txt    # List of dependencies
```

---

## 🎯 Features  

✅ **Add Customer and Bill Data**  
✅ **Store Data in MySQL Database**  
✅ **Retrieve and Display Bills in GUI**  
✅ **Responsive PySide6 UI**  

---

## 🔧 Configuration  

Ensure the correct **MySQL connection credentials** in `db.py`:  

```python
self.conn = pymysql.connect(
    host="localhost",  
    user="root",  
    password="",  # Replace with your MySQL password  
    database="billing_system"
)
```

---

## ▶️ Running the Application  

```sh
python billing_app.py
```

---

## 📝 How It Works  

1️⃣ Enter **Customer Name** and **Contact Number**.  
2️⃣ Add **Product Details** and **Total Amount**.  
3️⃣ Click **Save Bill** (Data is stored in MySQL).  
4️⃣ Click **View Bills** to retrieve saved bills.  

---

## 🤝 Contributing  

Feel free to contribute by:  
- Improving the UI  
- Adding features like **PDF bill generation**  
- Implementing **search & filter functionality**  

---

## 📩 Contact  

For queries, reach out via [email@example.com](mailto:email@example.com)  

🚀 **Happy Coding!**  
