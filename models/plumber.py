from database.connection import get_db_connection

class Plumber:
    def init(self, name, rate):
        self.name = name
        self.rate = rate

def save(self):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO plumbers(name, rate)
    VALUES (?, ?)
    ''', (self.name, self.rate))
    conn.commit()
    conn.close()

@staticmethod
def all():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM plumbers')
    plumbers = cursor.fetchall()
    conn.close()
    return plumbers

@staticmethod
def update(plumber_id, name, rate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE plumbers 
    SET name = ?, rate = ? 
    WHERE id = ?
    ''', (name, rate, plumber_id))
    conn.commit()
    conn.close()

@staticmethod
def delete(plumber_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM plumbers WHERE id = ?', (plumber_id,))
    conn.commit()
    conn.close()
