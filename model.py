import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_material(self, name, type, count):
        expaier = datetime.now()

        # Insert query with parameters
        self.cursor.execute(
            """
                INSERT INTO Materials (name_of_material, type_of_materials, count, expaier) 
                VALUES (?, ?, ?, ?)
            """, (name, type, count, expaier)
        )
        self.conn.commit()


