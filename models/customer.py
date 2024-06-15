from database.connection import get_db_connection

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO customers (name, email)
        VALUES (?, ?)
        ''', (self.name, self.email))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM customers
        ''')
        customers = cursor.fetchall()
        conn.close()
        return customers

    @staticmethod
    def update(customer_id, name, email): 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE customers
        SET name =?, email =?
        WHERE id =?
        ''', (name, email, customer_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(customer_id):  
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM customers
        WHERE id =?
        ''', (customer_id,))
        conn.commit()
        conn.close()     

