from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from db import Database

class BillingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()
        self.setWindowTitle("Billing System")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        # Customer Input
        self.name_label = QLabel("Customer Name:")
        self.name_input = QLineEdit()
        self.contact_label = QLabel("Contact Number:")
        self.contact_input = QLineEdit()
        
        # Product Input
        self.product_label = QLabel("Product Details:")
        self.product_input = QLineEdit()
        self.amount_label = QLabel("Total Amount:")
        self.amount_input = QLineEdit()
        
        # Buttons
        self.add_bill_button = QPushButton("Save Bill")
        self.view_bills_button = QPushButton("View Bills")
        
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.contact_label)
        self.layout.addWidget(self.contact_input)
        self.layout.addWidget(self.product_label)
        self.layout.addWidget(self.product_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.add_bill_button)
        self.layout.addWidget(self.view_bills_button)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

        self.add_bill_button.clicked.connect(self.save_bill)
        self.view_bills_button.clicked.connect(self.load_bills)

    def save_bill(self):
        name = self.name_input.text()
        contact = self.contact_input.text()
        product = self.product_input.text()
        amount = self.amount_input.text()

        if not name or not contact or not product or not amount:
            return
        
        # Insert customer if not exists
        customer_id = self.get_customer_id(contact)
        if not customer_id:
            self.db.execute("INSERT INTO customers (name, contact) VALUES (%s, %s)", (name, contact))
            customer_id = self.get_customer_id(contact)
        
        # Insert bill
        self.db.execute("INSERT INTO bills (customer_id, product_details, total_amount) VALUES (%s, %s, %s)", (customer_id, product, amount))
        print("Bill saved successfully!")

    def get_customer_id(self, contact):
        result = self.db.fetch("SELECT id FROM customers WHERE contact = %s", (contact,))
        return result[0][0] if result else None

    def load_bills(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Customer Name", "Contact", "Product", "Total Amount"])

        bills = self.db.fetch("""
            SELECT customers.name, customers.contact, bills.product_details, bills.total_amount 
            FROM bills
            INNER JOIN customers ON bills.customer_id = customers.id
        """)

        for row_index, row_data in enumerate(bills):
            self.table.insertRow(row_index)
            for col_index, col_value in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(col_value)))

if __name__ == "__main__":
    app = QApplication([])
    window = BillingApp()
    window.show()
    app.exec()
