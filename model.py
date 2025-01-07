import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_material(self, name, type, count, expaier):
        self.cursor.execute("INSERT INTO Materials (name_of_material, type_of_materials, count, expaier) VALUES (?, ?, ?, ?)", (name, type, count, expaier))
        self.conn.commit()#لكي يفعلي الاكوات على قاعده البيانات

    def get_material(self):
        self.cursor.execute('SELECT * FROM Materials')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        name = [col[1] for col in rows] 
        type = [col[2] for col in rows]
        count = [col[3] for col in rows] 
        expaier = [col[4] for col in rows]
        return name, type, count, expaier
    
