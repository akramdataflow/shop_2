import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()
        self.add_bill('23432','sdgdfg')
        self.add_bill_detales(invoice_id=3, material_name='del1', quantity="3", unit_price=234, total_price=22000)

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
        rows = self.cursor.fetchall()  
        defe_id = [col[0] for col in rows] 
        customer_name = [col[1] for col in rows] 
        phone_num = [str(col[2]) for col in rows]  # Convert to string
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



########################################################## اضافه فاتورة

    def add_bill(self, invoice_date, total_amount):
        self.cursor.execute("INSERT INTO Invoices (invoice_date, total_amount) VALUES (?, ?)", (invoice_date, total_amount))
        self.conn.commit()

##########################################################اضافة تفاصيل الفاتوره

    def add_bill_detales(self, invoice_id, material_name, quantity, unit_price, total_price):
        self.cursor.execute("INSERT INTO InvoiceDetails (invoice_id, material_name, quantity, unit_price, total_price) VALUES (?, ?, ?, ?, ?)", (invoice_id, material_name, quantity, unit_price, total_price))
        self.conn.commit()

    def get_bill_detales(self):
        self.cursor.execute('SELECT * FROM InvoiceDetails')
        rows = self.cursor.fetchall()  
        invoice_id = [str(col[1]) for col in rows] 
        material_name = [col[2] for col in rows] 
        quantity = [col[3] for col in rows]
        unit_price = [col[4] for col in rows] 
        total_price = [col[5] for col in rows]
        return invoice_id, material_name, quantity, unit_price, total_price
    


    def del_bill_detales(self, material_name):
        self.cursor.execute("DELETE FROM InvoiceDetails WHERE material_name = ?", (material_name,))
        self.conn.commit()

        #################################المشتريات
    def add_purc(self, price, company_name, bill_num, date):
        self.cursor.execute("INSERT INTO Purchases (price, company_name, bill_num, date) VALUES ( ?, ?, ?, ?)", (price, company_name, bill_num, date))
        self.conn.commit()#لكي يفعلي الاكوات على قاعده البيانات

    def get_purc(self):
        self.cursor.execute('SELECT * FROM Purchases')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        purc_id = [col[0] for col in rows] 
        price = [col[1] for col in rows] 
        company_name = [col[2] for col in rows]
        bill_num = [col[3] for col in rows] 
        date = [col[4] for col in rows]
        return purc_id,price, company_name, bill_num, date


    
    def del_purc(self, purc_id):
        self.cursor.execute("DELETE FROM Purchases WHERE id = ?", (purc_id,))
        self.conn.commit()  
 



       

        
    