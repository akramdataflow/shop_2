import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_material(self, name, type, count, expaier, price):
        self.cursor.execute("INSERT INTO Materials (name_of_material, type_of_materials, count, expaier, price) VALUES (?, ?, ?, ?, ?)", (name, type, count, expaier, price))
        self.conn.commit()#لكي يفعلي الاكوات على قاعده البيانات

    def get_material(self):
        self.cursor.execute('SELECT * FROM Materials')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        mat_id = [col[0] for col in rows] 
        name = [col[1] for col in rows] 
        type = [col[2] for col in rows]
        count = [col[3] for col in rows] 
        expaier = [col[4] for col in rows]
        price = [col[5] for col in rows]
        return mat_id, name, type, count, expaier, price
    
    
    def del_material(self, material_id):
        self.cursor.execute("DELETE FROM Materials WHERE id = ?", (material_id,))
        self.conn.commit()  # تنفيذ التغييرات في قاعدة البيانات

    
    def update_material(self, material_id, name, type, expaier, price):
        self.cursor.execute('''
            UPDATE Materials
            SET name_of_material = ?, type_of_materials = ?, expaier = ?, price = ?
            WHERE id = ?
        ''', (name, type, expaier, price, material_id))
        self.conn.commit()  # تنفيذ التغييرات في قاعدة البيانات

#######################################################دفع مؤجل 
   
    def add_Deferred(self, customer_name, phone_num, address , price):
        self.cursor.execute("INSERT INTO Deferred (customer_name, phone_num, address,  price) VALUES (?, ?, ?, ?)", (customer_name, phone_num, address, price))
        self.conn.commit()
        

        
    def get_Deferred(self):
        self.cursor.execute('SELECT * FROM Deferred')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        defe_id = [col[0] for col in rows] 
        customer_name = [col[1] for col in rows] 
        phone_num = [col[2] for col in rows]
        address = [col[3] for col in rows] 
        price = [col[4] for col in rows]
        
        return defe_id, customer_name, phone_num, address, price
    
    
    def del_Deferred(self, deferred_id):
        self.cursor.execute("DELETE FROM Deferred WHERE id = ?", (deferred_id,))
        self.conn.commit()



    def update_Deferred(self, deferred_id, customer_name, phone_num, address, price):
        self.cursor.execute('''
            UPDATE Deferred
            SET customer_name = ?,  phone_num = ?, address = ?, price = ?
            WHERE id = ?
        ''', (customer_name, phone_num, address, price, deferred_id))
        self.conn.commit()    
