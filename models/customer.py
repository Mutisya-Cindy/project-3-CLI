from database.connection import get_db_connection

class Customer:
    def init(self, name, contact):
        self.name = name
        self.contact = contact

def save(self):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO customers(name, contact)
    VALUES (?, ?)
    ''', (self.name, self.contact))
    conn.commit()
    conn.close()

@staticmethod
def all():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return customers

@staticmethod
def update(customer_id, name, contact):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE customers 
    SET name = ?, contact = ? 
    WHERE id = ?
    ''', (name, contact, customer_id))
    conn.commit()
    conn.close()

@staticmethod
def delete(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()