from database.connection import get_db_connection

class Booking:

    def __init__(self, customer_id, plumber_id, date):
        self.customer_id = customer_id
        self.plumber_id = plumber_id
        self.date = date

    def save (self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO bookings (customer_id, plumber_id, date)
        VALUES (?,?,?)
        ''', (self.customer_id, self.plumber_id, self.date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT b.id, c.name as customer_name, p.name as plumber_name, b.date
        FROM bookings b
        INNER JOIN customers c ON b.customer_id = c.id
        INNER JOIN plumbers p ON b.plumber_id = p.id
        ''')
        bookings = cursor.fetchall()
        conn.close()
        return bookings
    
    @staticmethod
    def update (customer_id, booking_id, plumber_id, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE bookings
        SET customer_id =?, plumber_id =?, date =?
        WHERE id =?
        ''', (customer_id, plumber_id, date, booking_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete (booking_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM bookings
        WHERE id =?
        ''', (booking_id,))
        conn.commit()
        conn.close()    
    
