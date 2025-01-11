from view import *
from model import *

class Controller:
    def __init__(self):
        self.view = MyView(self)
        self.model = Model()

    def show_list(self):
        self.show_list_add = Lists(self)
        self.show_list_add.show() 

    
    def show_sales(self):
        self.show_sales_add = Sales(self)
        self.show_sales_add.show() 

   


    def show_Purchases(self):
        self.show_Purchases_add = Purchases(self)
        self.show_Purchases_add.show() 

    def show_Deferred(self):
        self.show_Deferred_add = Deferred(self)
        self.show_Deferred_add.show() 



      
    def show_materials (self):
        self.show_materials_add =  Materials(self)
        self.show_materials_add.show() 

     
      
    def show_closet(self):
        self.show_closet_add = Closet(self)
        self.show_closet_add.show() 


         
    def show_Data_analysis(self):
        self.show_Data_analysis_add = Data_analysis(self)
        self.show_Data_analysis_add.show()

        #########################كونترول الحاصه بلمواد

    def del_mat_show(self):
        self.show_del_mat = DelMat(self)
        self.show_del_mat.show()

    def update_mat_show(self):
        self.show_update_mat = UpdateMat(self)
        self.show_update_mat.show()


    def add_material_to_model(self, name, type, count, expaier, price):
        self.model.add_material(name,type,count,expaier, price)

    def get_material_from_model(self):
        mat_id, name, type, count, expaier, price = self.model.get_material()
        return mat_id, name, type, count, expaier, price
    
    def del_material_from_model(self, material_id):
        self.model.del_material(material_id)
        self.show_materials()


    def update_material_to_model(self, material_id, name, type, expaier, price):
        self.model.update_material(material_id, name, type, expaier, price)
        self.show_materials()



        ################################################ كونترول المؤجل


        
    def del_defer_show(self):
        self.show_del_defer = DelDefer(self)
        self.show_del_defer.show()

    def update_defer_show(self):
        self.show_update_defer = UpdateDefer(self)
        self.show_update_defer.show()


    def add_Deferred_to_model(self, customer_name, phone_num, address, price):
        self.model.add_Deferred(customer_name, phone_num, address, price)

    def get_Deferred_from_model(self):
        defe_id, customer_name, phone_num, address, price = self.model.get_Deferred()
        return defe_id, customer_name, phone_num, address, price
    
    def del_Deferred_from_model(self,deferred_id):
        self.model.del_Deferred(deferred_id)
        self.show_Deferred()


    def update_Deferred_to_model(self, deferred_id, customer_name, phone_num, address, price):
        self.model.update_Deferred(deferred_id, customer_name, phone_num, address, price)
        self.show_Deferred()

###################################################################### كونترولر اضافة تفاصيل الفاتوره

    def del_bill_detales_show(self):
            self.show_del_bill_detales = DelListDetales(self)
            self.show_del_bill_detales.show()

    def get_bill_detales_from_model(self):
        return self.model.get_bill_detales()

    def del_bill_detales_from_model(self,material_name):
        self.model.del_bill_detales(material_name)
        self.show_list()

        ################################المبيعات للحذف والتعديل
    def del_Sels_show(self):
        self.show_del_Sels = Delsels(self)
        self.show_del_Sels.show()

    def update_Sels_show(self):
        self.show_update_Sels = Updatesels(self)
        self.show_update_Sels.show()



    

