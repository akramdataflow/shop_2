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


    def add_material_to_model(self, name, type, count, expaier):
        self.model.add_material(name,type,count,expaier)

    def get_material_from_model(self):
        name, type, count, expaier = self.model.get_material()
        return name, type, count, expaier




    

