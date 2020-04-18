'''
Created on 16-Apr-2020

@author: ila roy
'''
#OOPR-Prac-5
#OOPR-Prac-5
#Start writing you code here
import time 
from datetime import datetime, timedelta 
class GarmentOrder:
    garment_dict ={"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    def __init__(self,cloth_type,no_of_piece):
        self.__cloth_type=cloth_type
        self.__no_of_piece=no_of_piece
        self.__delivery_date=time.strftime("%d/%m/%Y")
        self.__order_date=None
    
    def get_cloth_type(self):
        return self.__cloth_type
    def get_no_of_piece(self):
        return self.__no_of_piece
    def get_order_date(self):
        return self.__order_date
    def get_delivery_date(self):
        return self.__delivery_date
    
    def take_order(self):
        x=0 
        for key,value in GarmentOrder.garment_dict.items():
            if self.__cloth_type==key:
                if value[0]>=self.__no_of_piece:
                    self.update_stock()
                    x=self.calculate_amount()
                    return x 
                else:
                    return -1
            else:
                return -1 
                
    def calculate_amount(self):
        amount=0 
        for key,value in GarmentOrder.garment_dict.items():
            if self.__cloth_type==key:
                price=value[1]
                break 
        amount=self.__no_of_piece*price 
        return amount 
        
    def update_stock(self):
        for key,value in GarmentOrder.garment_dict.items():
            if self.__cloth_type==key:
                n=value[2]
                pieces_availbale=value[0]
                value[0]=pieces_availbale-self.__no_of_piece
                break
        d=datetime.date.today()+datetime.timedelta(days=n)
        self.__order_date=time.strftime(d,"%d/%m/%Y")
        

g=GarmentOrder("shirt",10)
y=g.take_order()
print(y)