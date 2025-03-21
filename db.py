import pymysql

class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",  
            user="root",  
            password="Rounak@123",  # Enter your MySQL password  
            database="billing_system"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, values=None):
        self.cursor.execute(query, values or ())
        self.conn.commit()

    def fetch(self, query, values=None):
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()
